# CHAPTER 3: RESEARCH METHODOLOGY & SYSTEM DESIGN

## 3.1 Introduction
This chapter explains the methodology used in designing, developing, implementing, and testing the proposed mobile application for poultry egg temperature monitoring and security update notifications. The Egg Guardian system integrates physical microcontrollers, cloud APIs, and a mobile frontend to establish a secure, real-time cyber-physical loop (Protopappas, Bechtsis, & Tsotsolas, 2025). The following sections detail the research design, system development life cycle phases, functional and non-functional requirements, architectural topologies, UML design diagrams, hardware wiring schematics, and testing criteria.

## 3.2 Research Design
This study adopts a hybrid research design combining **Design and Development Research (DDR)** (Richey & Klein, 2014) with **Experimental Research** (Campbell & Stanley, 2015). 
*   **Design and Development Research**: Focusing on the systematic study of designing, developing, and evaluating software systems, DDR provides a structured framework for translating requirements into functional cyber-physical components (Hevner, March, Park, & Ram, 2004). This design is highly appropriate for developing a mobile application since it guides the engineering lifecycle from architectural modeling to active HMI layouts.
*   **Experimental Research**: Involves testing the physical subsystem under varying environmental thermal loads and network connectivity states. This allows the study to empirically measure sensor accuracy (MAE) and packet recovery rates during simulated Wi-Fi drops (Pacheco da Costa et al., 2023).

## 3.3 System Development Methodology
This study utilizes the **Iterative Development Model** (Larman & Basili, 2003) to build, refine, and validate the software components. The development lifecycle is structured into six phases:
1.  **Requirement Analysis**: Translating biological temperature constraints and security lifecycle needs into hardware and software specifications (Gatkal et al., 2025).
2.  **System Design**: Modeling database structures, message-passing sequences, use case flows, and hardware schematics.
3.  **Development**: Writing the C++ firmware for the ESP32, constructing the FastAPI server using Python, and building the Flutter mobile UI using Dart.
4.  **Testing**: Executing unit tests on API endpoints, testing MQTT broker transport latency, and verifying FCM notification delivery.
5.  **Deployment**: Uploading the backend API to the cloud, distributing the Flutter mobile app build, and flashing firmware onto edge microcontrollers.
6.  **Maintenance**: Monitoring historical logs, adjusting threshold hysteresis values, and pushing firmware security update notification strings.

## 3.4 Requirement Analysis

### 3.4.1 Functional Requirements
The system must execute the following functions to meet user needs:
*   **User Registration and Login**: Provide secure account creation and session authorization using JSON Web Tokens (JWT) (Lengkong et al., 2025).
*   **Display Real-Time Egg Storage Temperature**: Visualize current temperature readings captured by the DS18B20 digital sensor (Trust, 2026).
*   **Display Security Status**: Render device update alerts and firmware version mismatch warning banners in the mobile UI.
*   **Push Notifications for Abnormal Temperature**: Trigger system-level FCM alarms when temperatures cross the safe boundaries of $37.0^\circ\text{C}$ to $39.0^\circ\text{C}$ (FAO, 2024).
*   **Security Update Notifications**: Notify the operator when a firmware version mismatch is detected in the backend broker (Dr. Brindha S et al., 2025).
*   **Temperature History**: Render scrollable charts of historical temperature telemetry logged over time.
*   **User Profile Management**: Allow operators to modify threshold limits, user passwords, and notification preferences.

### 3.4.2 Non-Functional Requirements
*   **Fast Response Time**: End-to-end telemetry propagation and FCM alert notification delivery must take less than $2.0	ext{ seconds}$ (Nalendra & Waspada, 2025).
*   **Secure Authentication**: Passwords must be hashed using Bcrypt, and API route communication must require JWT validation (Verma & Ranga, 2018).
*   **High Availability**: The FastAPI server must handle asynchronous non-blocking connection requests from multiple edge nodes and mobile clients concurrently.
*   **User-Friendly Interface**: The Flutter application must incorporate modern UX practices, intuitive color scales (representing thermal zones), and clear alert banners (Adebayo, 2022).
*   **Scalability**: The backend database must support writing and reading historical telemetry logs across multiple facilities.
*   **Reliability**: The system must maintain data completeness during Wi-Fi drops by caching logs on the edge node buffer and flushing them on reconnect (Pacheco da Costa et al., 2023).

## 3.5 System Architecture

### 3.5.1 System Architecture Topology
The physical and virtual components are connected in a multi-tier cyber-physical topology.

```
Temperature Source (DS18B20 Probe)
        │
        ▼
 ESP32 Edge Node (Buffer Queue)
        │
        ▼ (MQTT TLS Port 8883)
 Backend/API (FastAPI Server)
        │
        ├────────────────────────┐
        ▼                        ▼
 Database (PostgreSQL)     Push Notification Service (FCM)
                                 │
                                 ▼
                          Mobile Application (Flutter UI)
```

Data flows through this architecture in a continuous sequence:
1.  The **DS18B20 digital temperature probe** captures thermal readings and transmits them to the **ESP32 microcontroller** (Trust, 2026).
2.  The ESP32 publishes the telemetry data over an encrypted **MQTT TLS channel** (port 8883) to the **FastAPI Backend/API** (Abdullah & Hamdan, 2023).
3.  The FastAPI server processes the payload, checks edge firmware versions, writes the record to the **PostgreSQL Database**, and broadcasts the data to active clients via WebSockets.
4.  If the temperature violates configured limits, the FastAPI backend sends an alert payload to the **Firebase Cloud Messaging (FCM) Service**, which pushes a system-level alarm to the **Flutter Mobile Application** (Dr. Brindha S et al., 2025).

Figure 3.1 illustrates this system architecture layout:

![Figure 3.1: Layered system architecture of the Egg Guardian system, illustrating the Physical/Sensing, Transport, Cloud Service, and HMI/Mobile layers.]C:/Users/USER/.gemini/antigravity/brain/6500ed53-115c-4abd-abcb-3c1580976dd6/system_architecture_diagram_1783789257793.png

## 3.6 System Design

### 3.6.1 Use Case Diagram
The Use Case diagram illustrates the interactions between the primary actors (Poultry Farm Operator and Backend Admin) and the application features.

Figure 3.5 shows the Use Case diagram:

![Figure 3.5: Use Case Diagram for the Egg Guardian mobile app.]C:/Users/USER/.gemini/antigravity/brain/6500ed53-115c-4abd-abcb-3c1580976dd6/use_case_diagram_1783877000546.png

### 3.6.2 Activity Diagram
The Activity diagram traces the control flow and decision-making logic of the system during data acquisition.

Figure 3.6 shows the Activity diagram:

![Figure 3.6: Activity Diagram showing system processing logic for network drops and alert states.]C:/Users/USER/.gemini/antigravity/brain/6500ed53-115c-4abd-abcb-3c1580976dd6/activity_diagram_1783877038773.png

### 3.6.3 Sequence Diagram
The Sequence diagram details the chronological message exchanges between the edge node, MQTT broker, FastAPI web engine, database, and HMI client.

Figure 3.2 outlines the UML Sequence diagram:

![Figure 3.2: Asynchronous UML Data Flow Sequence Diagram, illustrating message exchanges between the ESP32 node, MQTT broker, FastAPI backend, PostgreSQL database, and the Flutter mobile application via WebSockets and FCM.]C:/Users/USER/.gemini/antigravity/brain/6500ed53-115c-4abd-abcb-3c1580976dd6/data_flow_sequence_1783859443532.png

### 3.6.4 Entity Relationship Diagram (ERD)
The database ERD schema models the logical entities, primary keys, foreign keys, and relationships that structure storage.

Figure 3.3 illustrates the Database ERD schema:

![Figure 3.3: Entity-Relationship database schema diagram showing the tables, primary/foreign keys, and relational cardialities.]C:/Users/USER/.gemini/antigravity/brain/6500ed53-115c-4abd-abcb-3c1580976dd6/database_schema_1783859407387.png

### 3.6.5 Hardware Wiring Schematic
The hardware schematic details the electrical wiring, sensor connections, pull-up resistors, and relay actuator control pins.

Figure 3.4 shows the Hardware wiring diagram:

![Figure 3.4: Hardware wiring schematic showing the ESP32 NodeMCU, DHT22 and DS18B20 sensors, pull-up resistors, relay board, and AC heating/cooling actuators.]C:/Users/USER/.gemini/antigravity/brain/6500ed53-115c-4abd-abcb-3c1580976dd6/hardware_schematic_1783859385884.png

---

## 3.7 Development Tools and Technologies

### 3.7.1 Mobile Development
*   **Flutter (Dart)**: An open-source UI software development kit created by Google, used to compile the cross-platform Android and iOS application from a single codebase (Adebayo, 2022). It provides high-performance WebSocket listeners and charts widgets.

### 3.7.2 Backend
*   **FastAPI (Python)**: A modern, fast (high-performance) web framework for building APIs with Python 3.11. Pydantic handles validation, and Starlette handles ASGI routing, enabling asynchronous non-blocking connection processing.

### 3.7.3 Database
*   **PostgreSQL**: A powerful, open-source object-relational database system, utilized as the central repository to log historical temperature records, security alerts, and user profiles.

### 3.7.4 Programming Languages
*   **Dart**: Used for mobile UI widgets layouts and WebSocket client routines.
*   **Python**: Used for FastAPI endpoint logic, security checks, and database queries.
*   **C++ (Arduino IDE)**: Used to write the ESP32 firmware, managing the local sensor query loop, offline buffering, and MQTT connections.

### 3.7.5 Development Tools
*   **Android Studio**: The official integrated development environment (IDE) for Google's Android operating system, used to emulate mobile runs.
*   **Visual Studio Code**: A lightweight code editor used for writing Python backend API routines and Dart scripts.
*   **GitHub**: A Web-based Git repository hosting service used for source code version control and collaborative backups.

---

## 3.8 Database Design

### 3.8.1 Database Schema and Tables
The database consists of four tables designed to store telemetry logs, credentials, and alerts:

#### Table 3.1: Users Table Schema
| Attribute Name | Data Type | Constraints | Description |
|---|---|---|---|
| `id` | SERIAL | Primary Key | Unique internal user identifier |
| `email` | VARCHAR(255) | Unique, Not Null | User login credentials email address |
| `password_hash` | VARCHAR(255) | Not Null | Bcrypt hashed session password |
| `role` | VARCHAR(50) | Not Null | Authorization scope (Operator/Admin) |

#### Table 3.2: Temperature Records Table Schema
| Attribute Name | Data Type | Constraints | Description |
|---|---|---|---|
| `id` | SERIAL | Primary Key | Unique record identifier |
| `sensor_id` | VARCHAR(100) | Not Null | Hardware DS18B20 digital address string |
| `temperature` | NUMERIC(5, 2) | Not Null | Captured decimal temperature reading ($^\circ	ext{C}$) |
| `timestamp` | TIMESTAMP | Not Null | Database record ingestion time |

#### Table 3.3: Security Alerts Table Schema
| Attribute Name | Data Type | Constraints | Description |
|---|---|---|---|
| `id` | SERIAL | Primary Key | Unique warning alert identifier |
| `alert_type` | VARCHAR(100) | Not Null | Alert category string (e.g. Firmware Mismatch) |
| `message` | TEXT | Not Null | User-facing descriptive notification payload |
| `timestamp` | TIMESTAMP | Not Null | Occurrence timestamp of security event |

#### Table 3.4: Notifications Table Schema
| Attribute Name | Data Type | Constraints | Description |
|---|---|---|---|
| `id` | SERIAL | Primary Key | Unique identifier for notification track |
| `user_id` | INTEGER | Foreign Key | Reference mapping to Users PK (`id`) |
| `title` | VARCHAR(255) | Not Null | Mobile notification alert title header |
| `body` | TEXT | Not Null | Mobile notification alert body content |
| `status` | VARCHAR(50) | Not Null | Status flag (Delivered / Pending / Read) |

---

## 3.9 System Implementation

### 3.9.1 Login Page
The login page serves as the entry point for the mobile application. Operators input their email and password, which the Flutter app sends to the backend via HTTPS. If verified, the app receives a JWT token and saves it to secure storage to authorize subsequent requests.

### 3.9.2 Dashboard
The Dashboard acts as the primary cockpit for the poultry operator. It initializes WebSocket connections to the cloud backend to stream live temperature data and registers the FCM token to enable push notifications (Nalendra & Waspada, 2025).

### 3.9.3 Temperature Monitoring Screen
This screen displays real-time temperature readings on a color-coded gauge (Green: safe, Red: abnormal). It includes a historical line chart powered by the Flutter Syncfusion charting library, showing temperature trends over a 24-hour window.

### 3.9.4 Notification Screen
Displays a scrollable log of historical security update alerts and temperature threshold warnings, retrieving records from the backend API.

### 3.9.5 Settings Page
Allows farm administrators to adjust temperature threshold boundaries ($T_{	ext{min}}$, $T_{	ext{max}}$) and toggle push notification preferences.

### 3.9.6 Backend Integration
The integration connects the mobile app with the backend using WebSockets for real-time telemetry streaming and REST APIs for authentication and settings management.

---

## 3.10 Testing and Validation

### 3.10.1 Testing Methods
*   **Unit Testing**: Validating isolated functions, such as the ESP32 ring buffer enqueue logic and backend JWT signature parsing.
*   **Integration Testing**: Verifying the communication links between the ESP32 edge node, MQTT broker, and FastAPI backend API.
*   **System Testing**: Testing the end-to-end system from physical sensor read to mobile UI update.
*   **User Acceptance Testing (UAT)**: Under UAT, farm operators navigate the app to verify dashboard usability, historical chart readability, and alert responsiveness.

### 3.10.2 UAT Survey Structure (System Usability Scale)
The User Acceptance Testing is evaluated using the standardized 10-item Likert-scale System Usability Scale (SUS) questionnaire (Brooke, 1996). Ten operators evaluate the application across statements such as: "I found the system very easy to use" and "I would need the support of a technical person to be able to use this app."

The final SUS score ($S_{	ext{total}}$) is computed as follows:
*   For odd-numbered questions ($i \in \{1, 3, 5, 7, 9\}$):
    $$S_i = X_i - 1$$
    where $X_i$ is the user score (1 to 5).
*   For even-numbered questions ($i \in \{2, 4, 6, 8, 10\}$):
    $$S_i = 5 - X_i$$
*   The cumulative score is scaled to a value out of 100:
    $$S_{	ext{total}} = 2.5 	imes \sum_{i=1}^{10} S_i$$
A threshold score of $S_{	ext{total}} \ge 70$ is required to validate system readiness for field operations.

### 3.10.3 Evaluation Criteria
*   **Accuracy of Temperature Updates**: The DS18B20 sensor readings must align with a reference thermometer, maintaining an MAE $\le 0.5^\circ	ext{C}$ (Trust, 2026).
*   **Notification Delivery**: Notifications must arrive within $2.0	ext{ seconds}$ of a threshold breach (Nalendra & Waspada, 2025).
*   **Response Time**: WebSocket updates must refresh the dashboard charts in under $500	ext{ms}$.
*   **Usability**: The app must achieve an average System Usability Scale (SUS) score above 70 during UAT trials.
*   **Reliability**: The ESP32 local buffer must capture all telemetry points during Wi-Fi drops and flush them with 100% data recovery on reconnect (Pacheco da Costa et al., 2023).

---

## 3.11 Ethical Considerations

### 3.11.1 User Privacy
No personal data beyond the user's email address is collected. This minimizes the risk of exposing sensitive user information.

### 3.11.2 Data Security
All API route communications are secured with HTTPS and JWT authorization tokens. This ensures only authorized users can read historical logs or modify temperature configurations.

### 3.11.3 Secure Authentication
User passwords are encrypted with Bcrypt before storage in the PostgreSQL database, protecting user credentials in the event of a database compromise.

### 3.11.4 Data Confidentiality
Telemetry data is transmitted over encrypted channels (MQTTS/TLS port 8883) to prevent unauthorized interception.

---

## 3.12 Summary
This chapter explained the design and development methodology of the Egg Guardian system. It described the iterative development model, functional and non-functional requirements, system architecture, UML design diagrams, hardware wiring schematics, and testing criteria. The next chapter presents the implementation, results, and experimental evaluation.
