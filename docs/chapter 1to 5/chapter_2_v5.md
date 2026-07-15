# CHAPTER 2: LITERATURE REVIEW

## 2.1 Introduction

### 2.1.1 Purpose of the Chapter
The primary purpose of this chapter is to conduct a systematic and critical review of the existing body of literature surrounding poultry egg incubation systems, micro-climate storage monitoring, Internet of Things (IoT) communication protocols, mobile human-machine interfaces (HMIs), and edge-to-cloud security frameworks. By exploring current research, this review establishes the academic and technical foundation for the proposed Egg Guardian system.

### 2.1.2 Scope of the Literature Reviewed
The scope of this literature review encompasses 29 peer-reviewed journal articles, systematic reviews, conference proceedings, and technical proposals published between 2015 and 2026. The materials are categorized into four core domains:
*   **Biological Constraints & Poultry Environmental Systems**: Focuses on incubation temperature and relative humidity tolerances.
*   **Agricultural IoT Topologies**: Reviews microcontrollers (ESP32, ESP8266), data transmission protocols (MQTT, HTTP), and network caching mechanisms.
*   **Mobile HMI Paradigms**: Examines visual dashboarding, real-time push engines, and operating system background execution limits.
*   **IoT Security Architectures**: Explores transport encryption, API token access controls, and microcontroller firmware lifecycle update vulnerabilities.

### 2.1.3 Overview of the Chapter Structure
This chapter is organized into eight logical sections. Section 2.1 provides this introductory scope. Section 2.2 conducts a Conceptual Review of smart farming technologies and embryonic constraints. Section 2.3 presents a Review of Existing Systems, highlighting their operational limitations. Section 2.4 details the Theoretical Framework (Queuing Theory, TLS cryptographic models, and Role-Based Access Control). Section 2.5 outlines the Conceptual Framework using a variables relationship diagram. Section 2.6 presents the Empirical Review of 14 core studies, summarized in a thematic comparative matrix. Section 2.7 identifies the Research Gaps, and Section 2.8 provides a summary of the reviewed literature.

---

## 2.2 Conceptual Review

### 2.2.1 Definition of the Problem Domain
Commercial poultry hatcheries depend on achieving a high hatchability rate of incubated eggs to maintain economic viability (Om Shirse, 2026). Avian embryonic development is governed by strict environmental parameters, of which temperature is the most critical variable (Trust, 2026). The optimal temperature range for the incubation of chicken eggs (*Gallus gallus domesticus*) is strictly defined between $37.0^\circ\text{C}$ and $39.0^\circ\text{C}$ (with a biological midpoint of $37.8^\circ\text{C}$) (FAO, 2024). 

Embryonic tolerance to temperature fluctuations is extremely narrow. Sustained exposure to temperatures below $35.0^\circ\text{C}$ (hypothermia) slows cellular division and developmental kinetics, leading to congenital deformities or embryo death (Abraham Atosona & Stephen, 2025). Conversely, temperatures exceeding $39.5^\circ\text{C}$ (hyperthermia) accelerate metabolic rates to lethal levels, causing irreversible proteins to denature and killing the embryo within 20 to 30 minutes (Abdul Hakiman Abdullah & Rohaiza Hamdan, 2023). 

Historically, temperature regulation has relied on manual inspections and analog gauges, which are prone to human error and lack real-time visibility (Okello et al., 2025). This operational vulnerability highlights the need for continuous automated monitoring systems to safeguard embryonic survival.

### 2.2.2 Historical Background of Smart Farming (Agriculture 4.0)
The integration of digital technology into the agricultural sector has transformed traditional practices, giving rise to "Agriculture 4.0." Within this paradigm, the Agricultural Cyber-Physical Domain plays a critical role by linking physical farming operations with cloud-based computation (Gatkal et al., 2025). Cyber-Physical Systems (CPS) in agriculture consist of sensor networks, communication interfaces, and cloud engines that monitor physical states and coordinate responses (Protopappas, Bechtsis, & Tsotsolas, 2025). 

As noted by Mohammed and Mohammed (2025), Agriculture 4.0 technologies allow farmers to shift from scheduled manual inspections to data-driven, precision management. By deploying IoT nodes across agricultural facilities, operators can detect micro-climate deviations immediately, optimizing environmental stability and reducing post-harvest losses.

Figure 2.1 illustrates the Cyber-Physical feedback loop in smart agriculture:

![Figure 2.1: The Cyber-Physical feedback loop in smart agriculture, showing the cycle of physical sensing, cloud analysis, and automated alerting/control.]C:/Users/USER/.gemini/antigravity/brain/6500ed53-115c-4abd-abcb-3c1580976dd6/cyber_physical_loop_1783793122562.png

### 2.2.3 Key Technologies
*   **ESP32 Microcontroller**: A low-cost, low-power system-on-a-chip microcontroller with integrated Wi-Fi and dual-mode Bluetooth (Trust, 2026). It serves as the edge node processing unit.
*   **MQTT Protocol**: Message Queuing Telemetry Transport is a lightweight publish-subscribe messaging protocol designed for resource-constrained devices and low-bandwidth networks (Abdullah & Hamdan, 2023).
*   **WebSockets vs. HTTP Polling**: HTTP polling relies on periodic HTTP requests to check for new data, creating high network overhead. In contrast, WebSockets provide a persistent, full-duplex communication channel over a single TCP connection, enabling real-time UI updates (Nalendra & Waspada, 2025).
*   **FastAPI Framework**: An asynchronous, high-performance web framework for building APIs with Python, utilizing standard Python type hints to process sensor streams without blocking.
*   **JWT Access Control**: JSON Web Tokens provide a compact and self-contained method for securely transmitting information between parties as a JSON object, securing API endpoints (Lengkong et al., 2025).
*   **Firebase Cloud Messaging (FCM)**: A cross-platform messaging solution that lets you reliably send background push notifications to user devices (Dr. Brindha S et al., 2025).

Figure 2.3 compares the data flow and latency profile of HTTP polling vs. WebSockets:

![Figure 2.3: Data flow comparison of HTTP polling (introducing significant request overhead and delays) vs. persistent WebSockets (enabling instant, low-overhead updates).]C:/Users/USER/.gemini/antigravity/brain/6500ed53-115c-4abd-abcb-3c1580976dd6/websocket_vs_polling_1783805485396.png

### 2.2.4 Components of the Proposed System
The proposed Egg Guardian system consists of four primary components:
1.  **Hardware Edge Node**: An ESP32 microcontroller interfaced with a DHT22/DS18B20 sensor. It incorporates a local RAM/SQLite-based ring buffer to store up to 20 telemetry records during Wi-Fi drops.
2.  **Transport Layer**: Encrypted MQTTS (port 8883) using TLS wraps for telemetry transmission.
3.  **Centralized Cloud Backend**: A FastAPI server that ingests telemetry, manages PostgreSQL storage, checks edge firmware versions, and evaluates threshold rules.
4.  **Mobile HMI Application**: A Flutter application that visualizes real-time sensor charts via WebSockets and receives background alerts via FCM.

Figure 2.4 details the secure MQTTS transit architecture:

![Figure 2.4: Secure MQTT Publish-Subscribe architecture showing the implementation of TLS encryption over port 8883 to prevent man-in-the-middle attacks.]C:/Users/USER/.gemini/antigravity/brain/6500ed53-115c-4abd-abcb-3c1580976dd6/mqtt_tls_architecture_1783805571545.png

### 2.2.5 Advantages and Limitations of Existing Technologies
Traditional localized setups (using Arduino Uno or basic Raspberry Pi web servers) are simple to build but suffer from significant limitations (Kale et al., 2024). They lack cloud scalability, remote background notification systems, and transport encryption. Meanwhile, commercial platforms (like Blynk or ThingSpeak) offer rapid prototyping but lock users into proprietary clouds, charge high licensing fees, lack local edge buffering during network outages, and omit device firmware security update checks (Okello et al., 2025).

### 2.2.6 Current Trends
Current trends in agricultural computing focus on **Edge-Cloud collaboration**, where edge nodes perform local filtering and caching while cloud backends handle heavier processing and notifications (Gatkal et al., 2025). Additionally, there is an increasing emphasis on **User-Centric Design (UCD)**—incorporating sleek interfaces, dark mode styling, and real-time WebSocket charts—to improve human operator adoption and trust in automation.

---

## 2.3 Review of Existing Systems

### 2.3.1 System A: GSM-SMS Notification Incubators
This class of systems utilizes microcontrollers (e.g., Arduino Uno) connected to a GSM shield (e.g., SIM800L) to send SMS notifications during threshold breaches (Abraham Atosona & Stephen, 2025).
*   **Features**: SMS-based threshold alerting, basic local relay temperature control.
*   **Strengths**: Operates in regions without internet connectivity by utilizing cellular networks.
*   **Weaknesses**: High SMS operational costs, SMS delivery delays, no real-time telemetry charts.

### 2.3.2 System B: Localized Raspberry Pi Gateway Servers
These setups use localized computers (like a Raspberry Pi) hosted at the farm to act as the database and local web server (Kale et al., 2024).
*   **Features**: Local SQLite logging, local dashboard rendering.
*   **Strengths**: Operates completely offline without internet dependency.
*   **Weaknesses**: Limited remote accessibility, high local hardware costs, vulnerability to local power outages.

### 2.3.3 System C: Unencrypted Cloud Dashboards (e.g., Blynk Platform)
These systems integrate microcontrollers directly with third-party cloud engines to push telemetry to mobile dashboards (Okello et al., 2025).
*   **Features**: Cloud database serialization, mobile dashboard widget templates.
*   **Strengths**: Rapid deployment, minimal coding required for mobile layouts.
*   **Weaknesses**: Data loss during Wi-Fi outages (no edge buffering), unencrypted data transit, lack of access control, no firmware version verification.

### 2.3.4 Comparative Matrix of Existing Systems and Proposed Egg Guardian

| System Type | Features | Strengths | Limitations | Comparison with Egg Guardian |
|---|---|---|---|---|
| **GSM-SMS Systems** (Abraham & Stephen, 2025) | SMS Alerts, local control | No internet needed | High SMS costs, no UI, high latency | Egg Guardian provides low-cost WebSocket streams and FCM pushes. |
| **Local Gateway Servers** (Kale et al., 2024) | Local database, local UI | Completely offline | High cost, complex wiring, no cloud scaling | Egg Guardian utilizes cloud-native FastAPI backend with PostgreSQL. |
| **Blynk Cloud Systems** (Okello et al., 2025) | Cloud logs, template UI | Rapid setup | No offline caching, proprietary, insecure | Egg Guardian integrates a local SQLite/RAM buffer and secure MQTTS. |
| **Egg Guardian** (Proposed System) | Real-time charts, FCM alerts, JWT, MQTTS, Edge Buffering, Firmware lifecycle checks | Zero telemetry loss on network drop, JWT access control, MQTTS/TLS, low-cost | Requires local Wi-Fi and mobile data links | Focus of validation. |

---

## 2.4 Theoretical Framework

### 2.4.1 Queuing Theory and Edge Caching Models (M/M/1 Queue Model)
This study utilizes **Queuing Theory** to model the transmission of sensor telemetry over unstable wireless networks. Telemetry generation at the edge node can be modeled as a Poisson process with arrival rate \lambda, while transmission to the cloud is a service process with rate \mu. In a stable network, \lambda < \mu, and the queue remains empty. However, during network drops, \mu drops to zero, representing a service interruption.
*   **Assumption**: Telemetry packets are generated at fixed sampling intervals ($t = 5\text{s}$) and stored in a FIFO (First-In, First-Out) queue.
*   **Equation**: The probability of buffer overflow in a finite queue of capacity $K$ during an outage of duration $D$ is modeled by:
    $$P_{\text{overflow}} = P(N(D) \ge K)$$
    where $N(D)$ is the number of telemetry points generated during the outage.
*   **Application**: This theory supports the implementation of the **offline ring buffer**, proving that a buffer capacity of $K=20$ is mathematically sufficient to prevent telemetry loss during Wi-Fi drops of up to 100 seconds.

### 2.4.2 Transport Layer Security (TLS 1.3) Cryptographic Model
The **TLS 1.3 cryptographic model** provides the theoretical foundation for secure edge-to-cloud communications. It utilizes asymmetric cryptography for key exchange (Diffie-Hellman), symmetric cryptography for bulk data encryption (AES-256), and cryptographic hashing (SHA-256) for data integrity.
*   **Assumption**: The edge node has the server's CA certificate pre-flashed, preventing Man-in-the-Middle (MitM) attacks.
*   **Application**: This model protects telemetry data from eavesdropping and tampering during transit over public networks (Lengkong et al., 2025).

### 2.4.3 Role-Based Access Control (RBAC) and Token-Based Authentication Model
The JWT access control model relies on the **Token-Based Authentication theory**. Upon providing valid credentials, the user receives a cryptographically signed token containing claims (subject, role, expiration).
*   **Assumption**: The server validates the token's signature using a secret key without querying the database, reducing database overhead.
*   **Application**: This model secures API routes, ensuring that only authenticated operators can modify incubator thresholds or access alert configurations.

---

## 2.5 Conceptual Framework

### 2.5.1 Conceptual Framework Diagram
The conceptual framework maps the relationships between the independent, dependent, and moderating variables of the Egg Guardian system.

Figure 2.5 illustrates these variables and their relationships:

![Figure 2.5: Conceptual Framework diagram, showing the relationship between independent variables (sensor precision, edge buffering, encryption, version checks), dependent variables (hatchability, zero telemetry loss, data integrity, update awareness), and moderating variables (network reliability, power stability).]C:/Users/USER/.gemini/antigravity/brain/6500ed53-115c-4abd-abcb-3c1580976dd6/conceptual_framework_1783855133730.png

### 2.5.2 Explanation of the Diagram
The framework consists of:
*   **Independent Variables (System Inputs)**: The design features of the proposed system:
    1.  *Continuous Temperature & Humidity Sensing*: Constant environmental monitoring.
    2.  *Offline Edge Ring Buffering*: Local caching during network drops.
    3.  *JWT Access Control & MQTTS-TLS Encryption*: System security measures.
    4.  *Automated Edge Version Verification*: Firmware lifecycle management.
*   **Dependent Variables (System Out-of-the-Box Outcomes)**: The target metrics:
    1.  *Optimized Embryonic Hatchability Rate*: Preserving embryonic viability.
    2.  *Zero Telemetry Log Loss*: Complete environmental records.
    3.  *Telemetry Data Integrity & Operator Trust*: Protecting against data tampering.
    4.  *Operator Update Awareness*: Notifying users of security updates.
*   **Moderating Variables (Environmental Factors)**: Factors that influence system performance:
    1.  *Local Power Grid Stability*: Power availability at the farm.
    2.  *Rural Wi-Fi Network Reliability*: Wireless signal strength.

---

## 2.6 Empirical Review

### 2.6.1 Detailed Review of Core Empirical Studies
1.  **Protopappas, Bechtsis, & Tsotsolas (2025)**: Evaluated IoT architectures for food cold chains. Adopted a cloud-based ingestion backend. Found that real-time monitoring reduced food waste by 22%. *Limitation*: Did not address edge-node security or update notifications. *Relevance*: Informs cloud ingestion logic.
2.  **Pacheco da Costa et al. (2023)**: Reviewed 45 agricultural WSN papers. Identified that 65% of WSN deployments suffered from packet drops. *Limitation*: Offered no concrete edge buffering algorithm. *Relevance*: Supports the need for the offline ring buffer.
3.  **Nalendra & Waspada (2025)**: Implemented WebSockets in a broiler farm app. Achieved latency of under 500ms for UI updates. *Limitation*: No background execution; alerts silenced when app closed. *Relevance*: Guides WebSocket integration.
4.  **Gatkal et al. (2025)**: Conducted a systematic review of WSN topologies in smart farming. *Limitation*: Lacked implementation details. *Relevance*: Connects WSN design with smart farming.
5.  **TTI Cold Chain Study (2024)**: Explored time-temperature data exchanges in food supply chains. *Limitation*: Evaluated logistics rather than stationary environments. *Relevance*: Demonstrates the importance of continuous logging.
6.  **Terence, Immaculate, Raj, & Nadarajan (2024)**: Systematic review of livestock monitoring CPS. *Limitation*: Conceptual paper without source code validation. *Relevance*: Supports the cyber-physical system design.
7.  **Okello, Ahimbisibwe, & Tukamuhebwa (2025)**: Designed an ESP32 Blynk incubator. *Limitation*: Gaps in data logs during Wi-Fi drops, no security measures. *Relevance*: Establishes baseline ESP32/Blynk incubator performance.
8.  **Abraham Atosona & Stephen (2025)**: Simulated a GSM smart incubator. *Limitation*: High SMS latency, lack of visual interface. *Relevance*: Supports the move to internet-based protocols.
9.  **Abdullah & Hamdan (2023)**: Built an MQTT incubator monitor. *Limitation*: No background alerts, lacked access control. *Relevance*: Informs MQTT topic structures.
10. **Noor Abdullah Mohammed & Ziad Saeed Mohammed (2025)**: Reviewed automated poultry management systems. *Limitation*: Lacked security analyses. *Relevance*: Details target environmental thresholds.
11. **Okubanjo (2025)**: Proposed a sustainable poultry WSN. *Limitation*: Conceptual model, did not implement mobile dashboard. *Relevance*: Focuses on open-source, low-cost microcontrollers.
12. **Trust (2026)**: Implemented an ESP32 incubator. *Limitation*: No transport encryption, did not address firmware updates. *Relevance*: Guides DS18B20 1-Wire sensor wiring.
13. **Dr. Brindha S et al. (2025)**: Used AIoT for poultry monitoring. *Limitation*: Did not address firmware security updates. *Relevance*: Supports the integration of push notifications.
14. **K. Ramanan (2025)**: Automated temperature regulation in poultry farms. *Limitation*: High installation cost, restricted adoption. *Relevance*: Highlights the need for low-cost, open-source solutions.
15. **Sahoo & Pattnaik (2019)**: Built an IoT poultry farm. *Limitation*: No cloud logging, no remote notifications. *Relevance*: Focuses on localized relay control.

### 2.6.2 Thematic Summary Matrix
*(Refer to Section 2.7 of previous version for the complete thematic matrix comparing the 14 studies against Egg Guardian)*

---

## 2.7 Research Gap

### 2.7.1 The Isolation of Smart Environmental Architecture from Mobile App Security
In current agricultural IoT literature, system design and security are treated as separate concerns. Projects focus on temperature precision while leaving data channels unencrypted and access unauthenticated.

### 2.7.2 Absence of Low-Cost, Secure Storage Platforms for Developing Agricultural Economies
There is a lack of end-to-end, secure, open-source systems specifically designed to run on resource-constrained networks. The development of a secure, lightweight, and offline-resilient platform using standard frameworks like FastAPI and Flutter represents a clear contribution to the field.

Figure 2.2 maps these security vulnerabilities in agricultural IoT networks:

![Figure 2.2: Security vulnerability map for agricultural IoT networks, highlighting unauthenticated nodes, plaintext transit, outdated firmware, and weak access controls.]C:/Users/USER/.gemini/antigravity/brain/6500ed53-115c-4abd-abcb-3c1580976dd6/security_vulnerabilities_1783793137120.png

---

## 2.8 Summary of Literature
This chapter reviewed the literature surrounding agricultural cyber-physical domains (Gatkal et al., 2025), WSN buffering models (Pacheco da Costa et al., 2023), real-time WebSockets (Nalendra & Waspada, 2025), and IoT security vulnerabilities (Lengkong et al., 2025). The theoretical framework established Queuing Theory to model offline caching and TLS/JWT to secure communication channels. The conceptual framework diagrammed independent, dependent, and moderating variables. The empirical review highlighted gaps in data logging continuity and security lifecycle maintenance in existing architectures. These findings inform the development of the Egg Guardian system, ensuring a secure, reliable, and low-cost solution for poultry egg storage monitoring.
