import asyncio
import json
from datetime import datetime, timezone
import os

os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///./test.db"

async def test_mqtt_logic():
    from app.database import async_session_maker, engine, Base
    from app.services.mqtt import MQTTService
    
    # Init DB
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
    # Setup mock data
    async with async_session_maker() as db:
        from app.models import Device, AlertRule, User
        device = Device(device_id="eggpod-01", name="eggpod-01")
        db.add(device)
        await db.flush()
        
        rule = AlertRule(device_id=device.id, temp_min=35.0, temp_max=39.0)
        db.add(rule)
        
        user = User(email="test@example.com", hashed_password="pw", is_superuser=True, is_active=True, fcm_token="dummy_token")
        db.add(user)
        await db.commit()

    # Run mqtt logic
    mqtt = MQTTService()
    async with async_session_maker() as db:
        try:
            print("Running _persist_telemetry...")
            await mqtt._persist_telemetry(db, "eggpod-01", 45.0, datetime.now(timezone.utc))
            await db.commit()
            print("Successfully ran _persist_telemetry")
        except Exception as e:
            print(f"Exception caught: {e}")
            import traceback
            traceback.print_exc()
            
    # Check if alert was created
    async with async_session_maker() as db:
        from app.models import Alert, Telemetry
        from sqlalchemy import select
        result = await db.execute(select(Alert))
        alerts = result.scalars().all()
        print(f"Total alerts in DB: {len(alerts)}")
        
        result = await db.execute(select(Telemetry))
        telemetrys = result.scalars().all()
        print(f"Total telemetry in DB: {len(telemetrys)}")

asyncio.run(test_mqtt_logic())
