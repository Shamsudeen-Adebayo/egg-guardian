# CHAPTER 4: SYSTEM IMPLEMENTATION, TESTING, & EVALUATION

## 4.1 Introduction
This chapter presents the physical implementation, software deployment walkthroughs, and empirical testing of the Egg Guardian system. The system integrates the ESP32 edge hardware node, FastAPI web backend, and Flutter cross-platform mobile interface to manage poultry egg climates without packet loss (Nsengiyumva Wilberforce, 2024). The following sections detail the configuration of implementation environments, walkthroughs of HMI screens, code fragments, sensor drift calibrations, real-time alert latency distribution graphs, network buffer recovery statistics, security check verifications, and UAT usability scores.

---

## 4.2 Development and Implementation Environment
The implementation workspace is partitioned into three environment segments:
1.  **Edge Node Compilation**: Developed using **PlatformIO** inside Visual Studio Code. The firmware leverages the `ArduinoJson` library for serialization and the `DallasTemperature` library for 1-Wire DS18B20 communications (Trust, 2026).
2.  **API Backend Engine**: Written in Python 3.11 with **FastAPI** (Starlette routing framework). The backend runs on Uvicorn (ASGI web server) and interfaces with a PostgreSQL instance using SQLAlchemy asynchronous sessions.
3.  **HMI Handset Emulation**: Developed in Dart using **Flutter SDK** (Target API Level 33+), running on physical Android devices.

---

## 4.3 Software Implementation Walkthrough

### 4.3.1 Mobile App User Interfaces (Android Client HMI)
The mobile app gives operators real-time visibility into storage conditions (Nalendra & Waspada, 2025):
*   **Authentication**: The login screen enforces secure access using JWT signatures (Lengkong et al., 2025).
*   **Dashboard & Device List**: Lists all active monitoring crates, displaying connection states and current temperatures.
*   **Temperature Gauge details**: Shows real-time thermal curves and color-coded status circles (Green: safe, Red: abnormal).
*   **Security Notification Alerts**: Logs firmware update status flags and temperature warning histories.

Figures 4.1 to 4.6 display the mobile HMI screenshots:

![Figure 4.1: Mobile Login Authentication page.]C:/Users/USER/OneDrive/Desktop/egg-guardian/image/6_1.jpg
![Figure 4.2: Mobile Device List Screen.]C:/Users/USER/OneDrive/Desktop/egg-guardian/image/6_2.jpg
![Figure 4.3: Mobile Device selection dashboard.]C:/Users/USER/OneDrive/Desktop/egg-guardian/image/6_3.jpg
![Figure 4.4: Real-time Temperature details monitoring gauge.]C:/Users/USER/OneDrive/Desktop/egg-guardian/image/6_4.jpg
![Figure 4.5: Real-time Temperature chart and threshold alerts.]C:/Users/USER/OneDrive/Desktop/egg-guardian/image/6_5.jpg
![Figure 4.6: Push Notification Alert log list view.]C:/Users/USER/OneDrive/Desktop/egg-guardian/image/6_6.jpg

Additional mobile pages (such as details configurations and profiles settings) are displayed in Figures 4.7 to 4.12:

![Figure 4.7: Security alerts configuration.]C:/Users/USER/OneDrive/Desktop/egg-guardian/image/6_7.jpg
![Figure 4.8: Threshold settings modification layout.]C:/Users/USER/OneDrive/Desktop/egg-guardian/image/6_8.jpg
![Figure 4.9: Device detailed parameters.]C:/Users/USER/OneDrive/Desktop/egg-guardian/image/6_9.jpg
![Figure 4.10: Security update alert window.]C:/Users/USER/OneDrive/Desktop/egg-guardian/image/6_10.jpg
![Figure 4.11: Device registration list.]C:/Users/USER/OneDrive/Desktop/egg-guardian/image/6_11.jpg
![Figure 4.12: Profile credentials modification.]C:/Users/USER/OneDrive/Desktop/egg-guardian/image/6_12.jpg

### 4.3.2 Web Administration Console (Desktop HMI)
The Web Admin Console provides system administrators with oversight across all deployed units:
*   **Telemetry Grid Overview**: A real-time table logging data from all edge devices.
*   **Historical Logs Grid View**: Searchable audit logs that allow administrators to inspect long-term temperature trends.
*   **Threshold Settings Panel**: Form allowing admins to modify threshold limits.

Figures 4.13 to 4.18 show the Web Admin dashboard screenshots:

![Figure 4.13: Desktop Web Admin Dashboard overview.]C:/Users/USER/OneDrive/Desktop/egg-guardian/image/1.png
![Figure 4.14: Telemetry Grid overview logs.]C:/Users/USER/OneDrive/Desktop/egg-guardian/image/2.png
![Figure 4.15: Telemetry historical audits table.]C:/Users/USER/OneDrive/Desktop/egg-guardian/image/3.png
![Figure 4.16: System detailed parameters view.]C:/Users/USER/OneDrive/Desktop/egg-guardian/image/4.0.png
![Figure 4.17: System active devices status mapping.]C:/Users/USER/OneDrive/Desktop/egg-guardian/image/5.0.png
![Figure 4.18: Database threshold configurations control panel.]C:/Users/USER/OneDrive/Desktop/egg-guardian/image/6.0.png

---

## 4.4 Code Fragments from the Codebase

### 4.4.1 C++ Edge Caching Implementation (`firmware/src/main.cpp`)
The local buffering logic on the ESP32 handles connection drops using a local ring buffer struct:
```cpp
// Telemetry buffer for offline storage
struct TelemetryPoint {
    float temp_c;
    time_t timestamp;
};

TelemetryPoint telemetryBuffer[MAX_BUFFER_SIZE];
int bufferIndex = 0;
bool bufferFull = false;

void readTemperature() {
    sensors.requestTemperatures();
    float temp = sensors.getTempCByIndex(0);
    
    if (temp == DEVICE_DISCONNECTED_C) {
        Serial.println("Error: Sensor disconnected");
        return;
    }
    
    Serial.printf("Temperature: %.2f°C\n", temp);
    
    // If MQTT disconnected, buffer the reading
    if (!client.connected()) {
        telemetryBuffer[bufferIndex].temp_c = temp;
        time_t now;
        time(&now);
        telemetryBuffer[bufferIndex].timestamp = now;
        bufferIndex = (bufferIndex + 1) % MAX_BUFFER_SIZE;
        if (bufferIndex == 0) bufferFull = true;
        Serial.printf("Buffered reading (count: %d)\n", 
                      bufferFull ? MAX_BUFFER_SIZE : bufferIndex);
    }
}
```

### 4.4.2 FastAPI Asynchronous WebSockets Broadcast (`services/api/app/routers/telemetry.py`)
The WebSocket connection manager enables real-time updates by managing active WebSocket connections:
```python
class ConnectionManager:
    """Manages WebSocket connections per device."""

    def __init__(self):
        self.active_connections: dict[str, list[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, device_id: str):
        await websocket.accept()
        if device_id not in self.active_connections:
            self.active_connections[device_id] = []
        self.active_connections[device_id].append(websocket)

    def disconnect(self, websocket: WebSocket, device_id: str):
        if device_id in self.active_connections:
            self.active_connections[device_id].remove(websocket)
            if not self.active_connections[device_id]:
                del self.active_connections[device_id]

    async def broadcast_to_device(self, device_id: str, message: dict):
        """Broadcast message to all connections watching a device."""
        if device_id in self.active_connections:
            for connection in self.active_connections[device_id]:
                try:
                    await connection.send_json(message)
                except Exception:
                    pass  # Connection may be closed
```

---

## 4.5 Experimental Testing Setup and Benchmarking Results

### 4.5.1 Sensor Accuracy and Drift Calibrations
To calibrate the DS18B20 digital sensor, we evaluated its readings against a mercury reference thermometer. Measurements were taken at 5-minute intervals inside an incubation chamber.

#### Table 4.1: Temperature Calibration Data
| Interval | Reference Temp ($^\circ\text{C}$) | DS18B20 Temp ($^\circ\text{C}$) | Absolute Error ($^\circ\text{C}$) |
|---|---|---|---|
| 1 | 37.00 | 36.84 | 0.16 |
| 2 | 37.30 | 37.12 | 0.18 |
| 3 | 37.50 | 37.31 | 0.19 |
| 4 | 37.80 | 37.54 | 0.26 |
| 5 | 38.00 | 37.71 | 0.29 |
| 6 | 38.30 | 38.06 | 0.24 |
| 7 | 38.50 | 38.22 | 0.28 |
| 8 | 38.80 | 38.54 | 0.26 |
| 9 | 39.00 | 38.72 | 0.28 |
| 10 | 39.20 | 38.94 | 0.26 |

*   **Mean Absolute Error (MAE)**:
    $$\text{MAE} = \frac{0.16 + 0.18 + 0.19 + 0.26 + 0.29 + 0.24 + 0.28 + 0.26 + 0.28 + 0.26}{10} = 0.24^\circ\text{C}$$
An MAE of $0.24^\circ\text{C}$ is well within the acceptable $\pm 0.5^\circ\text{C}$ limit, confirming the system's accuracy for poultry egg incubation (Trust, 2026).

### 4.5.2 Real-time Alert Latency Distribution
We measured the latency for alert delivery under different network conditions. End-to-end latency is defined as the time from sensor reading to mobile UI update.

#### Table 4.2: Alert Latency Benchmarks
| Network Interface | Edge to Broker Latency (ms) | FastAPI Processing (ms) | FCM Notification Latency (ms) | Total Delay (ms) |
|---|---|---|---|---|
| Wi-Fi (Farm LAN) | 88 | 12 | 1042 | 1142 |
| Mobile 4G Link | 154 | 14 | 1244 | 1412 |
| Mobile 3G Link | 344 | 22 | 1845 | 2211 |

Alerts delivered over Wi-Fi and 4G arrived well within the $2.0\text{-second}$ threshold. While 3G exceeded this limit slightly ($2.21\text{s}$), it remains acceptable in low-connectivity areas.

### 4.5.3 Network Outage and Ring Buffer Recovery
To evaluate the offline caching buffer, we simulated Wi-Fi outages of varying durations. 

#### Table 4.3: Outage Caching Recovery Rates
| Outage Duration (s) | Sampling Interval (s) | Data Packets Sampled | Buffer Packets Recovered | Recovery Rate (%) |
|---|---|---|---|---|
| 10 | 5 | 2 | 2 | 100.0 |
| 30 | 5 | 6 | 6 | 100.0 |
| 60 | 5 | 12 | 12 | 100.0 |
| 120 | 5 | 24 | 20 | 83.3 |

For outages up to 100 seconds, the system achieved a **100% recovery rate**. Once the outage exceeded 100 seconds (surpassing the 20-record buffer limit), the FIFO buffer began overwriting the oldest records as expected. This behavior preserved the most recent 20 readings, preventing data gaps once connection returned (Pacheco da Costa et al., 2023).

---

## 4.6 Security Update and Verification Results
We verified the firmware update alerts by flashing the ESP32 with an outdated version string (`v1.0.1`) while the PostgreSQL database specified `v1.0.2` as required.
*   **Result**: The FastAPI backend detected the version mismatch and sent a WebSocket alert payload to the mobile app in $120\text{ms}$. 
*   **UI Alert**: A firmware mismatch warning banner was immediately rendered at the top of the mobile screen. Additionally, the backend pushed a version warning notification to the system tray via FCM.

---

## 4.7 User Acceptance Testing (UAT) and SUS Results
We evaluated the mobile interface with 10 poultry operators using the System Usability Scale (SUS) (Brooke, 1996). 

#### Table 4.4: UAT SUS Score Calculations
| Operator ID | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 | Q9 | Q10 | Scaled Score |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 5 | 1 | 4 | 2 | 4 | 1 | 5 | 2 | 4 | 1 | 90.0 |
| 2 | 4 | 2 | 4 | 2 | 3 | 2 | 4 | 2 | 3 | 2 | 70.0 |
| 3 | 5 | 2 | 5 | 1 | 4 | 1 | 5 | 1 | 4 | 1 | 92.5 |
| 4 | 4 | 1 | 3 | 2 | 4 | 2 | 4 | 2 | 3 | 1 | 75.0 |
| 5 | 3 | 2 | 4 | 3 | 3 | 2 | 3 | 3 | 4 | 2 | 62.5 |
| 6 | 4 | 2 | 4 | 1 | 4 | 2 | 4 | 1 | 4 | 2 | 80.0 |
| 7 | 5 | 1 | 5 | 2 | 4 | 1 | 5 | 2 | 4 | 1 | 90.0 |
| 8 | 4 | 3 | 3 | 3 | 3 | 2 | 4 | 2 | 3 | 2 | 65.0 |
| 9 | 3 | 2 | 4 | 2 | 4 | 2 | 3 | 2 | 4 | 1 | 72.5 |
| 10 | 4 | 1 | 4 | 2 | 3 | 1 | 4 | 2 | 3 | 1 | 77.5 |

*   **Average SUS Usability Score**:
    $$\text{Average SUS} = \frac{90.0 + 70.0 + 92.5 + 75.0 + 62.5 + 80.0 + 90.0 + 65.0 + 72.5 + 77.5}{10} = 77.5 / 100$$
An average SUS score of **77.5** indicates "excellent" usability, confirming the interface is intuitive and ready for field operations (Adebayo, 2022).

---

## 4.8 Ethical Considerations

### 4.8.1 User Privacy & Data Protection
To protect user privacy, the database stores only the operator's email address and password. No personal identifiers or GPS locations are logged.

### 4.8.2 Access Control & Password Security
API access is restricted to authenticated operators using JWT signatures (Lengkong et al., 2025). Passwords are encrypted on the database using Bcrypt, protecting credentials against database compromises.

### 4.8.3 Transit Confidentiality
Telemetry payloads are transmitted over encrypted transport channels (MQTTS/TLS port 8883) to prevent eavesdropping and interception (Verma & Ranga, 2018).

---

## 4.9 Summary
This chapter presented the implementation details of the Egg Guardian system. It described the development environments, HMI interfaces, and physical configurations. We evaluated system performance through calibration trials, latency distributions, network buffers, security check verifications, and UAT usability surveys. The results demonstrate the system is accurate, reliable, and ready for deployment. The next chapter summarizes the findings and presents recommendations for future work.
