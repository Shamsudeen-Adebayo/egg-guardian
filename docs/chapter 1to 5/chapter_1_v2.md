# CHAPTER 1: INTRODUCTION

## 1.1 Background of the Study

### 1.1.1 Overview of Poultry Production and Biological Constraints of Egg Storage
Poultry production stands as a cornerstone of global agriculture, providing an essential source of low-cost, high-quality animal protein in the form of meat and eggs to feed an expanding global population (Okubanjo, 2025). Within this sector, commercial poultry hatcheries rely heavily on achieving a high hatchability rate of incubated eggs to maintain economic viability and meet market demand (Om Shirse, 2026). Avian embryonic development is a complex, delicate physiological process governed by strict environmental parameters, of which temperature is the most critical variable (Trust, 2026). 

According to the Food and Agriculture Organization (FAO, 2024), the optimal temperature range for the incubation of chicken eggs (*Gallus gallus domesticus*) is strictly defined between $37.0^\circ\text{C}$ and $39.0^\circ\text{C}$ (with a biological midpoint of $37.8^\circ\text{C}$). Embryonic tolerance to temperature fluctuations is extremely narrow compared to other livestock domains (Mohammed & Mohammed, 2025). 

Sustained exposure to temperatures below $35.0^\circ\text{C}$ (hypothermia) slows cellular division and developmental kinetics, leading to congenital deformities, structural abnormalities, or complete embryo death (Abraham & Stephen, 2025). Conversely, temperatures exceeding $39.5^\circ\text{C}$ (hyperthermia) accelerate metabolic rates to lethal levels, causing irreversible proteins to denature and killing the embryo within 20 to 30 minutes (Abdul Hakiman Abdullah & Rohaiza Hamdan, 2023). 

Figure 1.1 illustrates these temperature thresholds and their corresponding biological zones:

![Figure 1.1: Biological temperature thresholds and viability zones for chicken egg incubation. Optimal development occurs strictly within the 37–39°C range.](C:/Users/USER/.gemini/antigravity/brain/6500ed53-115c-4abd-abcb-3c1580976dd6/temperature_zones_diagram_1783789242417.png)

Historically, temperature regulation in agricultural storage facilities has relied on manual inspections and analog gauges, which are prone to human error and lack real-time visibility (Okello et al., 2025). This operational vulnerability highlights the need for continuous automated monitoring systems to safeguard embryonic survival.

### 1.1.2 The Paradigm Shift to Agriculture 4.0 and Smart Farming Systems
The agricultural sector is undergoing a digital transformation known as "Agriculture 4.0." This shift is characterized by the integration of Cyber-Physical Systems (CPS), the Internet of Things (IoT), cloud computing, and big data analytics into daily farm operations (Gatkal et al., 2025). In smart farming, physical environments are continuously monitored by networks of connected sensors, creating a feedback loop where environmental variables inform digital models (Protopappas, Bechtsis, & Tsotsolas, 2025). 

As noted by Mohammed and Mohammed (2025), Agriculture 4.0 technologies allow farmers to shift from scheduled manual inspections to data-driven, precision management. By deploying IoT nodes across agricultural facilities, operators can detect micro-climate deviations immediately, optimizing environmental stability and reducing post-harvest losses.

### 1.1.3 The Role of Internet of Things (IoT) and Mobile Applications in Environmental Automation
The Internet of Things (IoT) provides the physical infrastructure for modern environmental monitoring. Microcontrollers, such as the ESP32, act as edge processing units that interface directly with digital sensors (e.g., DS18B20 or DHT22) to capture local micro-climate data (Trust, 2026). These edge nodes convert physical parameters into digital payloads and transmit them using lightweight protocols like MQTT (Message Queuing Telemetry Transport) over local wireless networks (Abdullah & Hamdan, 2023).

Mobile applications serve as the primary human-machine interface (HMI) in these systems. By using persistent communication channels like WebSockets, mobile apps can receive telemetry streams and update visual charts in real time (Nalendra & Waspada, 2025). This allows farm operators to monitor remote storage conditions from anywhere, receiving instant push notifications if parameters drift outside safe limits (Dr. Brindha S et al., 2025).

---

## 1.2 Problem Statement

### 1.2.1 Inefficiencies and Late Responses of Manual Monitoring and Standalone Gauges
Traditional poultry hatcheries rely on standalone thermometers or manual inspection schedules (Okubanjo, 2025). This approach creates large gaps in monitoring, particularly during night shifts or weekends (Om Shirse, 2026). If a heating element or ventilation fan fails, hours can pass before the issue is detected, exposing sensitive embryos to extreme temperatures and leading to high mortality rates (Okello et al., 2025).

Furthermore, manual inspection requires physically opening the incubator doors, which disrupts the internal micro-climate (humidity and temperature equilibrium) and causes further developmental stress to the embryos (Okello et al., 2025).

### 1.2.2 Micro-climate Deviations and Resulting Economic/Post-Harvest Losses
For commercial poultry operations, temperature deviations in incubators represent a significant financial risk. A single equipment failure that goes unnoticed for even short intervals can destroy an entire batch of eggs, causing severe financial losses, disrupting poultry supply chains, and threatening the operational viability of the farm (Okubanjo, 2025; Pacheco da Costa et al., 2023). 

To mitigate these losses, farms require a monitoring system with sub-2-second latency to notify off-site operators the moment a temperature threshold is breached.

### 1.2.3 Vulnerabilities, Lack of Access Control, and Lack of Remote Capabilities in Existing Farming Apps
While various smart farming applications exist, they often suffer from significant architectural weaknesses. Many current solutions use unencrypted communication protocols (such as standard HTTP or plain MQTT) and lack robust authentication, leaving them vulnerable to data interception and spoofing attacks (Lengkong et al., 2025). 

Furthermore, these applications often lack role-based access control (RBAC), allowing unauthorized users to modify temperature thresholds or disable critical alerting systems (Kale et al., 2024).

### 1.2.4 The Security Gap: Omission of Firmware and Mobile Security Update Notifications
A major vulnerability in agricultural IoT systems is the lack of ongoing software maintenance. Microcontroller firmware and mobile applications are rarely updated once deployed, leaving them exposed to security exploits (Dr. Brindha S et al., 2025). Most agricultural monitoring systems lack a mechanism to verify software versions or notify operators when a security patch is available, leaving devices vulnerable to unauthorized access and network hijacks.

If an attacker gains control of the edge node, they can spoof telemetry data (e.g. reporting an optimal 37.8°C while the actual temperature is dropping to lethal levels), masking incubator failures and leading to total batch losses (Lengkong et al., 2025).

---

## 1.3 Research Aim and Objectives

### 1.3.1 Research Aim
The primary aim of this research is to design, develop, and evaluate a secure, real-time IoT-based mobile application framework (named **Egg Guardian**) for monitoring poultry egg incubator temperature and delivering automated firmware and application security update notifications.

### 1.3.2 Specific Research Objectives
To comply with standard undergraduate research limits (Research Proposal Outline, 2023), the objectives are consolidated into exactly four key areas:
1.  **Hardware Edge Node Design**: Build an ESP32-based hardware edge node that interfaces with DS18B20/DHT22 sensors and features an offline ring buffer to prevent telemetry data loss during connectivity drops.
2.  **Unified Backend and HMI Development**: Design and implement a centralized cloud backend using FastAPI to process telemetry, coupled with a cross-platform Flutter mobile application to display real-time readings and receive push notifications.
3.  **Security Subsystem Implementation**: Integrate cryptographic access controls (JWT), secure transport layers (MQTTS/TLS), and an automated edge firmware lifecycle tracking system to notify users of security updates.
4.  **Experimental Evaluation and Validation**: Benchmark and evaluate the system's end-to-end latency, database ingestion reliability, local caching capability, and the propagation speed of firmware security alerts.

### 1.3.3 Alignment of Project Aim and Objectives with Identified Gaps
```
  Identified Gaps (Chapter 1.2)           Aligned Specific Objectives (Chapter 1.3.2)
+------------------------------------+   +------------------------------------+
| Manual checks, slow response times | ->| Obj 2: Unified Backend & HMI       |
+------------------------------------+   +------------------------------------+
| Data loss during network drops      | ->| Obj 1: ESP32 Offline Ring Buffer   |
+------------------------------------+   +------------------------------------+
| Spoofing & unencrypted channels    | ->| Obj 3: Security & Update Systems   |
+------------------------------------+   +------------------------------------+
| Outdated firmware, security gaps   | ->| Obj 4: Experimental Evaluation     |
+------------------------------------+   +------------------------------------+
```

---

## 1.4 Significance of the Study

### 1.4.1 Optimization of Post-Harvest Durability and Quality for Farm Operations
By providing sub-second telemetry transmission and immediate background alerting, this system enables poultry farm operators to respond to heating or ventilation failures before embryonic damage occurs (Okubanjo, 2025). This level of environmental control maximizes hatch rates, protects animal welfare, and improves the hatchery's overall productivity (Om Shirse, 2026).

### 1.4.2 Cost-Effective Scalability for Small-to-Mid Scale Poultry Farms
Unlike expensive proprietary systems, the proposed solution utilizes open-source frameworks (FastAPI, Flutter) and low-cost, off-the-shelf microcontrollers (ESP32). This approach allows small and mid-scale poultry hatcheries to deploy a professional monitoring solution without high licensing fees or complex installations (Trust, 2026; Abdullah & Hamdan, 2023).

### 1.4.3 Introduction of Security and Device Integrity Awareness in Agricultural Computing
This research addresses a critical gap in smart farming by demonstrating how security updates and device lifecycle management can be integrated directly into agricultural software (Lengkong et al., 2025). This establishes a template for building secure IoT networks in the agricultural domain (Dr. Brindha S et al., 2025).

---

## 1.5 Scope and Limitations of the Research

### 1.5.1 Technical Scope
The technical scope of the project encompasses:
*   **Hardware Layer**: An ESP32 microcontroller interfaced with a DS18B20 1-Wire temperature sensor or a DHT22 thermodynamic sensor (Trust, 2026; Shirse, 2026).
*   **Transport Layer**: MQTT over TCP, utilizing secure MQTTS (port 8883) for encrypted telemetry transmission (Abdullah & Hamdan, 2023).
*   **Cloud Layer**: A Python-based FastAPI backend, utilizing SQLAlchemy for object-relational mapping and a PostgreSQL database.
*   **HMI Layer**: A cross-platform Flutter application targeted for Android devices and a companion HTML5/Vanilla JS web dashboard (Nalendra & Waspada, 2025).

Figure 1.2 shows the systems architecture and data flow:

![Figure 1.2: General systems architecture mapping the data flow from the incubator sensor node to the FastAPI cloud backend and the mobile/web interfaces.](C:/Users/USER/.gemini/antigravity/brain/6500ed53-115c-4abd-abcb-3c1580976dd6/system_architecture_diagram_1783789257793.png)

### 1.5.2 Operational Limits
The system is designed for stationary egg storage and incubator environments and requires a local Wi-Fi connection at the hatchery site (Okello et al., 2025). Mobile monitoring and push alerts require cellular data or internet connectivity for the operator's smartphone. The current prototype does not monitor eggs in transit during shipping or logistics (Pacheco da Costa et al., 2023).

---

## 1.6 Operational Definition of Technical Terms

*   **Agriculture 4.0**: The integration of digital technologies, such as IoT and cloud computing, to automate and optimize agricultural production (Gatkal et al., 2025).
*   **Asynchronous I/O**: A programming model that allows a server to handle multiple operations concurrently without blocking execution, critical for high-frequency sensor streams.
*   **Bcrypt**: A secure, salt-based password hashing algorithm used to store user credentials.
*   **Cyber-Physical System (CPS)**: A system where physical mechanisms are controlled and monitored by computer-based algorithms (Protopappas et al., 2025).
*   **JSON Web Token (JWT)**: An open standard (RFC 7519) that defines a compact, secure way to transmit information between parties as a JSON object, used for user authentication.
*   **MQTT (Message Queuing Telemetry Transport)**: A lightweight publish-subscribe messaging protocol designed for resource-constrained devices and low-bandwidth networks (Abdullah & Hamdan, 2023).
*   **Over-The-Air (OTA)**: The wireless delivery of software updates or firmware patches to remote devices.
*   **Telemetry**: The automatic measurement and wireless transmission of environmental data from remote sources.
*   **WebSocket**: A protocol that provides full-duplex, real-time communication channels over a single TCP connection, enabling instant UI updates (Nalendra & Waspada, 2025).
