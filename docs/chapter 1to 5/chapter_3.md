# CHAPTER 3: RESEARCH METHODOLOGY & SYSTEM DESIGN

## 3.1 Overview of the Research Methodology
This research adopts an **applied engineering and experimental prototyping methodology** combined with quantitative performance evaluation and qualitative usability reviews. The study is structured around five core phases:
1.  **Requirements Formulation**: Defining environmental threshold limits, networking tolerances, and security compliance constraints.
2.  **Hardware Edge Node Fabrication**: Wiring sensor nodes, configuring dual-relay actuators, and developing an offline ring-buffering algorithm on the ESP32.
3.  **Cloud Backend & Transport Engineering**: Designing an asynchronous FastAPI server, setting up a PostgreSQL database schema, and configuring an MQTT broker with TLS encryption.
4.  **HMI Application Development**: Building a Flutter cross-platform mobile application utilizing WebSockets for real-time sensor streams and FCM for background notifications.
5.  **Experimental Validation**: Benchmarking sensor drift, end-to-end alert delivery latency, and network recovery rates under simulated Wi-Fi drops.

---

## 3.2 Requirements Analysis

### 3.2.1 Functional Requirements
The system must satisfy the following core operational functions:
*   **Continuous Climate Telemetry**: Capture temperature ($\pm 0.5^\circ	ext{C}$ accuracy) and humidity ($\pm 2\%$ accuracy) at 5-second sampling intervals.
*   **Offline Data Buffering**: Automatically store up to 20 telemetry records locally on the ESP32 during network drops and flush them once Wi-Fi reconnects.
*   **Asynchronous Alerting**: Deliver push notifications to the user's mobile device within 2 seconds of a threshold violation.
*   **Secure API Endpoint Access**: Restrict write operations on threshold configs and user registration using token-based access control.
*   **Firmware Verification**: Check the edge node's firmware version against the cloud database on handshake and display a warning banner in the mobile app if a mismatch is detected.

### 3.2.2 Non-Functional Requirements
*   **Performance Latency**: Cumulative latency for alert delivery must remain under $2.0	ext{ seconds}$.
*   **Reliability**: Telemetry recovery rate must be $100\%$ for connection drops lasting up to 100 seconds (capacity limit of the 20-record local buffer).
*   **Security Posture**: Plaintext transit of sensor data is prohibited; all communication channels must utilize TLS 1.3 encryption wrappers.
*   **Battery and Data Efficiency**: Minimize payloads (MQTT keep-alive packets under 128 bytes) to reduce network bandwidth and conserve power.

### 3.2.3 Hardware & Software Specifications
*   **Edge Node SoC**: ESP32 NodeMCU development board (32-bit dual-core, 520 KB SRAM, integrated 2.4 GHz Wi-Fi).
*   **Sensors**: DHT22 relative humidity sensor and DS18B20 high-precision digital temperature probe.
*   **Actuators**: Dual-channel 5V relay module interfacing a 220V heating lamp and a 12V exhaust fan.
*   **Cloud Stack**: Python 3.11, FastAPI backend web framework, PostgreSQL database, and EMQX/Mosquitto MQTT broker.
*   **Mobile HMI Stack**: Flutter cross-platform framework and Dart runtime environment.

---

## 3.3 System Architecture Design

### 3.3.1 Layered System Architecture
The Egg Guardian system utilizes a **four-layer cyber-physical architecture** to partition concerns between the physical environment, transport services, cloud computation, and human-machine interface layers.

Figure 3.1 illustrates this layered system architecture:

![Figure 3.1: Layered system architecture of the Egg Guardian system, illustrating the Physical/Sensing, Transport, Cloud Service, and HMI/Mobile layers.]C:/Users/USER/.gemini/antigravity/brain/6500ed53-115c-4abd-abcb-3c1580976dd6/system_architecture_diagram_1783789257793.png

### 3.3.2 Asynchronous Data Flow Sequence
To support real-time data flows and alert evaluation, the system utilizes asynchronous, non-blocking message-passing loops.

Figure 3.2 outlines this asynchronous message-passing sequence:

![Figure 3.2: Asynchronous UML Data Flow Sequence Diagram, illustrating message exchanges between the ESP32 node, MQTT broker, FastAPI backend, PostgreSQL database, and the Flutter mobile application via WebSockets and FCM.]C:/Users/USER/.gemini/antigravity/brain/6500ed53-115c-4abd-abcb-3c1580976dd6/data_flow_sequence_1783859443532.png

### 3.3.3 Database Entity-Relationship (ERD) Schema
The relational database schema is structured to log historical telemetry, manage user accounts, store threshold configurations, and track firmware releases.

Figure 3.3 illustrates the database ERD schema:

![Figure 3.3: Entity-Relationship database schema diagram showing the tables, primary/foreign keys, and relational cardialities.]C:/Users/USER/.gemini/antigravity/brain/6500ed53-115c-4abd-abcb-3c1580976dd6/database_schema_1783859407387.png

---

## 3.4 Hardware Subsystem Implementation and Wiring

### 3.4.1 Schematic Diagram and Pin Mappings
The hardware edge node centers around the ESP32 development board, which regulates power distribution and processes digital sensor outputs.
*   **DHT22 Sensor**: Connected to GPIO pin 4 (3.3V power, GND).
*   **DS18B20 Sensor**: Connected to GPIO pin 15 (3.3V power, GND) with a $4.7	ext{ k}\Omega$ pull-up resistor between data and VCC.
*   **Relay Board**: Relay 1 (Heating) connected to GPIO pin 18. Relay 2 (Cooling Fan) connected to GPIO pin 19.

Figure 3.4 shows the hardware wiring schematic:

![Figure 3.4: Hardware wiring schematic showing the ESP32 NodeMCU, DHT22 and DS18B20 sensors, pull-up resistors, relay board, and AC heating/cooling actuators.]C:/Users/USER/.gemini/antigravity/brain/6500ed53-115c-4abd-abcb-3c1580976dd6/hardware_schematic_1783859385884.png

### 3.4.2 Actuator Hysteresis Control Logic
To prevent relay chatter (rapid switching near threshold values that damages relays and equipment), the system implements a hysteresis control algorithm.

The state of the heating relay ($S_H \in \{0, 1\}$) is governed by:
$$S_H(t) = egin{cases} 1 & 	ext{if } T(t) < T_{	ext{target\_min}} \ 0 & 	ext{if } T(t) \ge T_{	ext{target\_mid}} \ S_H(t-\Delta t) & 	ext{if } T_{	ext{target\_min}} \le T(t) < T_{	ext{target\_mid}} \end{cases}$$

The state of the cooling fan relay ($S_C \in \{0, 1\}$) is governed by:
$$S_C(t) = egin{cases} 1 & 	ext{if } T(t) > T_{	ext{target\_max}} \ 0 & 	ext{if } T(t) \le T_{	ext{target\_mid}} \ S_C(t-\Delta t) & 	ext{if } T_{	ext{target\_mid}} < T(t) \le T_{	ext{target\_max}} \end{cases}$$

Where $T(t)$ represents the current sensor reading, $T_{	ext{target\_min}} = 37.0^\circ	ext{C}$, $T_{	ext{target\_max}} = 39.0^\circ	ext{C}$, and $T_{	ext{target\_mid}} = 37.8^\circ	ext{C}$.

---

## 3.5 Software Subsystem & Security Architecture Design

### 3.5.1 FastAPI Endpoint Configuration
The cloud backend exposes REST endpoints for core operations:
*   `POST /auth/register` and `/auth/login`: Account creation and verification, returning a JWT token signed with an HMAC-SHA256 key.
*   `GET /telemetry/history`: Retrieves historical telemetry logs (requiring JWT authorization).
*   `PUT /config/thresholds`: Updates target environmental thresholds (requiring JWT authorization).
*   `GET /firmware/check`: Verifies the firmware version string sent by the edge node.

### 3.5.2 Offline Buffer Queuing Algorithm
The ESP32 firmware manages connection drops using a local FIFO queue. During normal operations (Wi-Fi connected), telemetry is published directly to the MQTT broker. If a connection loss is detected, the firmware redirects telemetry writes to the local queue.
*   **Buffering Logic**:
    ```cpp
    struct TelemetryPoint {
      float temperature;
      float humidity;
      uint32_t timestamp;
    };
    TelemetryPoint ringBuffer[20];
    int head = 0;
    int tail = 0;
    int count = 0;

    void enqueue(TelemetryPoint point) {
      if (count < 20) {
        ringBuffer[head] = point;
        head = (head + 1) % 20;
        count++;
      } else {
        // Discard oldest (overwrite tail)
        ringBuffer[head] = point;
        head = (head + 1) % 20;
        tail = (tail + 1) % 20;
      }
    }
    ```
*   **Dequeuing Logic**: Once Wi-Fi connectivity returns, the node publishes all queued records sequentially before resuming real-time data transmission.

### 3.5.3 Cryptographic Security and OTA Update Handshake
*   **Transport Layer (MQTTS)**: Encrypted TCP connection using TLS 1.3 over port 8883.
*   **Authentication (JWT)**: Users authenticate with their passwords (hashed on the database using Bcrypt). The backend returns a JWT token that expires in 60 minutes.
*   **Firmware Mismatch Warning**: When the ESP32 publishes its current firmware version string ($V_{	ext{edge}}$) via MQTT, the FastAPI backend checks it against the target firmware version ($V_{	ext{required}}$) stored in the database. If $V_{	ext{edge}} < V_{	ext{required}}$, the backend pushes a version warning to the Flutter client UI via WebSockets and sends an update warning notification via FCM.
