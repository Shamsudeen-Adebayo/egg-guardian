# CHAPTER 2: LITERATURE REVIEW

## 2.1 Overview of Agricultural Cyber-Physical Domains
The integration of digital technology into the agricultural sector has transformed traditional practices, giving rise to "Agriculture 4.0." Within this paradigm, the Agricultural Cyber-Physical Domain plays a critical role by linking physical farming operations with cloud-based computation (Gatkal et al., 2025). Cyber-Physical Systems (CPS) in agriculture consist of sensor networks, communication interfaces, and cloud engines that monitor physical states and coordinate responses (Protopappas, Bechtsis, & Tsotsolas, 2025). As highlighted in the systematic review by Terence, Immaculate, Raj, and Nadarajan (2024), cyber-physical structures are particularly crucial in food supply chains and environmental cold chains. Their study demonstrates that continuous data flows from sensor nodes to centralized databases reduce physical parameter drift. 

Earlier, Wolfert, Ge, Verdouw, and Bogaardt (2017) explored the role of big data in smart farming, mapping the conceptual shift from localized agricultural tools to interconnected network layers that form regional farm management networks. Unlike traditional monitoring systems that collect data for simple storage, modern CPS platforms establish a continuous feedback loop. Environmental sensors measure physical conditions and transmit the data to a cloud backend, which evaluates the telemetry and coordinates actions to keep parameters within safe limits (Terence et al., 2024). This structural linkage between computing elements and physical entities defines the operational scope of modern agricultural automation, turning passive measurements into active controls.

In egg storage and incubator systems, this feedback loop acts as the primary defense against thermal shock. Embryonic development is not a static process; it undergoes daily metabolic shifts, requiring adaptive climate adjustments (Mohammed & Mohammed, 2025). By mapping the incubator as a cyber-physical system, environmental anomalies can be processed at the cloud layer to trigger localized actuators (such as exhaust fans or heating relays) while simultaneously alerting human operators.

Figure 2.1 illustrates this agricultural cyber-physical feedback loop:

![Figure 2.1: The Cyber-Physical feedback loop in smart agriculture, showing the cycle of physical sensing, cloud analysis, and automated alerting/control.](C:/Users/USER/.gemini/antigravity/brain/6500ed53-115c-4abd-abcb-3c1580976dd6/cyber_physical_loop_1783793122562.png)

By establishing this feedback loop, poultry operations can maintain stable incubator environments, reducing micro-climate drift and improving overall hatchery performance (Mohammed & Mohammed, 2025).

## 2.2 Theoretical Review of Embedded Wireless Networks and Supply Line Monitoring
Embedded wireless sensor networks (WSNs) form the communication backbone of smart agricultural monitoring. These networks operate under strict theoretical constraints, balancing range, power consumption, and packet delivery reliability (Gatkal et al., 2025). WSN nodes typically use low-power protocols like Zigbee, LoRa, or Wi-Fi to transmit telemetry to localized gateways or cloud brokers (Pacheco da Costa et al., 2023). In logistics, TTI Cold Chain Study (2024) notes that time-temperature indicators and continuous data exchanges are necessary to optimize food supply chains and verify product safety.

A key challenge in WSN design for agricultural applications is maintaining data completeness over unstable connections. Agricultural environments, particularly rural areas, often suffer from frequent Wi-Fi and power drops (Okello et al., 2025). To prevent data loss during these drops, edge nodes must implement queuing mechanisms, such as local ring buffers, to temporarily store data and flush it once connectivity is restored (Pacheco da Costa et al., 2023). In their theoretical outline, Research Proposal Design Framework (2023) established that data integrity constraints in remote monitoring are critical to achieving statistical significance in agricultural studies. 

Furthermore, Kamilaris, Kartakoullis, and Prenafeta-Boldú (2017) discussed how data transmission protocols affect the overall analytics cycle, arguing that raw unbuffered data streams generate high error rates in resource-constrained environments where packet drops are common. In rural environments where cellular or Wi-Fi networks have poor signal strength, telemetry loss can create gaps in historical records. This lack of complete data makes it difficult for algorithms to accurately predict equipment wear or diagnose system failures, demonstrating the need for offline edge buffers.

## 2.3 Methodological Review of IoT-Based Temperature Logging and Smart Farming Infrastructure
Modern smart farming infrastructure utilizes microcontrollers like the ESP32 and ESP8266 as low-cost edge processing units (Okubanjo, 2025). These microcontrollers capture environmental data and publish it to central servers using protocols like MQTT (Abdullah & Hamdan, 2023). Nsengiyumva Wilberforce and Dr. Johnson Mwebaze (2024) proposed an IoT-enabled smart agriculture framework utilizing these microcontrollers to improve crop yield monitoring in low-resource environments. Additionally, Ray, Dash, and De (2017) reviewed early IoT-based smart agricultural models, highlighting that lightweight publish-subscribe protocols reduce processing overhead at the gateway level.

Methodologies for logging this telemetry generally fall into two categories:
1.  **Localized Web Servers**: Using local gateways (such as a Raspberry Pi) to host database instances and log data locally (Kale et al., 2024). While this ensures offline reliability, it lacks the scalability and remote accessibility needed for multi-facility operations. Kumar and Singh (2018) demonstrated that local servers face significant availability risks if the hardware experiences local outages or power surges.
2.  **Centralized Cloud Backends**: Directing edge node telemetry to a cloud backend (such as a FastAPI server) that handles database logging and rules evaluation (Okubanjo, 2025). This approach offers global scalability but requires robust offline buffering on the edge nodes to survive connectivity drops.

The choice of communication protocols also has significant methodological implications. While HTTP is widely used, its verbose header structures and synchronous request-response model generate high network overhead (Ray et al., 2017). In contrast, MQTT uses a binary packet format and a publish-subscribe model, reducing data payloads by up to 80% (Abdullah & Hamdan, 2023). This makes MQTT highly suitable for resource-constrained edge microcontrollers that transmit telemetry over cellular links.

## 2.4 Evaluation of Specialized Systems: Poultry and Egg Storage Environments
Maintaining stable temperatures in poultry egg storage and incubator environments is critical, as deviations from the optimal 37–39°C range can quickly kill developing embryos (FAO, 2024). Researchers have proposed various automated monitoring solutions to address this requirement.

Abraham Atosona and Stephen (2025) designed a smart incubator that used a GSM module to send SMS notifications during temperature anomalies. However, SMS delivery times often exceeded 10 seconds, which is too slow to prevent cell death during rapid thermal changes. Om Shirse (2026) developed a low-cost ESP8266 and DHT22 monitoring system that significantly improved smallholder hatchery yields. Similarly, Abdullah & Hamdan (2023) built an MQTT-based incubator monitor that provided live visual feedback. 

A common limitation of these systems is the lack of an offline data buffer. When Wi-Fi connections drop, these architectures lose telemetry data, creating gaps in environmental logs (Okello et al., 2025; Trust, 2026). Additionally, these designs do not address security concerns like access control or unencrypted data transmission, leaving them vulnerable to tampering.

In large-scale chicken coops, Broiler Monitoring Journal (2024) validated that continuous logging of temperature and humidity variables reduces mortality rates in broilers. K. Ramanan (2025) proposed a temperature regulation system for poultry farms using IoT and automation, but noted that high installation costs restricted its adoption. Earlier, Malaysia IoT Study (2020) demonstrated a simple temperature and humidity monitor for poultry coops using basic IoT protocols, highlighting the long-term trend toward digital integration in poultry logistics.

To address remote hatchery management, Sahoo and Pattnaik (2019) built an IoT-based smart poultry farming system that focused on environmental parameter adjustment using relays. However, their system lacked cryptographic protection or mobile notifications. Soeb, Mamun, Shammi, Uddin, and Eimon (2021) fabricated a low-cost incubator to evaluate hatching performance of eggs, illustrating that stable, microprocessor-controlled temperatures are direct predictors of hatchability.

## 2.5 Comprehensive Critique of Mobile Applications in Smart Agriculture

### 2.5.1 Core Visual Dashboard Systems vs. Active Control Ecosystems
Many current agricultural mobile apps function as simple visual dashboards. They retrieve telemetry by periodically polling an HTTP API (e.g., every 30 seconds), which introduces significant latency and consumes excessive mobile data (Nalendra & Waspada, 2025). 

In contrast, active control systems use persistent WebSocket connections. This allows the backend to push new telemetry directly to the app UI the moment it is received, providing real-time visual updates and reducing mobile bandwidth usage by up to 60% (Nalendra & Waspada, 2025). Modern interaction design research suggests that real-time visual updates and dynamic UI updates improve operator trust and system usability in high-stress agricultural applications.

Figure 2.3 compares the data flow and latency profile of HTTP polling vs. WebSockets:

![Figure 2.3: Data flow comparison of HTTP polling (introducing significant request overhead and delays) vs. persistent WebSockets (enabling instant, low-overhead updates).](C:/Users/USER/.gemini/antigravity/brain/6500ed53-115c-4abd-abcb-3c1580976dd6/websocket_vs_polling_1783805485396.png)

### 2.5.2 Flaws in Data Visualization Models Lacking Background Execution
A common limitation in agricultural monitoring apps is the lack of background alert execution. If the user closes the application, the polling loop terminates, silencing alerts. Integrating background engines, such as Firebase Cloud Messaging (FCM), is essential to guarantee alert delivery when the application is not active in the foreground (Dr. Brindha S et al., 2025). 

Without background execution capabilities, a mobile application is highly vulnerable to operating system task termination. Modern mobile operating systems (such as Android and iOS) actively close background processes to conserve battery. If an application relies solely on an active UI loop to listen for alerts, the user will not receive alerts once the OS terminates the app. Using FCM addresses this limitation, routing notifications through system-level daemons that remain active even when the application is closed.

## 2.6 Security Concerns in IoT and Mobile Computing Environments

### 2.6.1 Weak Authentication Models and Lack of Access Control
To minimize code size and memory footprint, agricultural IoT nodes often omit device authentication (Lengkong et al., 2025). This allows attackers to send spoofed telemetry payloads directly to the backend database, potentially masking actual equipment failures and leading to hatch losses. Verma and Ranga (2018) conducted a comprehensive review of IoT security vulnerabilities, demonstrating that weak access control at the edge layer allows unauthorized users to intercept and spoof sensory outputs.

Figure 2.2 illustrates these common security vulnerabilities in agricultural IoT networks:

![Figure 2.2: Security vulnerability map for agricultural IoT networks, highlighting unauthenticated nodes, plaintext transit, outdated firmware, and weak access controls.](C:/Users/USER/.gemini/antigravity/brain/6500ed53-115c-4abd-abcb-3c1580976dd6/security_vulnerabilities_1783793137120.png)

Implementing secure authentication protocols, such as JSON Web Tokens (JWT) for APIs and TLS-encrypted handshakes for MQTT brokers, is essential to prevent unauthorized access and data tampering (Lengkong et al., 2025).

### 2.6.2 Unencrypted Telemetry Transmissions and Vulnerability to Data Tampering
Broadcasting telemetry over unencrypted HTTP or MQTT channels exposes systems to man-in-the-middle (MitM) attacks. Eavesdroppers can capture operational data or intercept and modify threshold configurations, leading to incubator failures. To prevent this, data transit must use TLS-encrypted wrappers, as detailed in Figure 2.4:

![Figure 2.4: Secure MQTT Publish-Subscribe architecture showing the implementation of TLS encryption over port 8883 to prevent man-in-the-middle attacks.](C:/Users/USER/.gemini/antigravity/brain/6500ed53-115c-4abd-abcb-3c1580976dd6/mqtt_tls_architecture_1783805571545.png)

Implementing transport layer encryption (MQTTS on port 8883) prevents eavesdropping and protects against data modification. Combined with signature checks at the API layer, this ensures that telemetry data remains confidential and authentic from the edge node to the backend database.

### 2.6.3 Software Lifecycle Gaps: Omission of Firmware and System Update Notifications
Once deployed in agricultural settings, IoT microcontrollers are rarely updated, leaving them exposed to firmware-level vulnerabilities over time (Dr. Brindha S et al., 2025). Most smart farming systems do not track firmware versions or notify operators when a security patch is available. Incorporating version verification and update alerts into the primary mobile app interface is critical to maintaining network security (Lengkong et al., 2025). 

As Wortmann and Flüchter (2015) point out, the long-term viability and value-add of IoT technology depend on managing device lifecycles, which requires secure remote updates and system integrity verification. When a vulnerability is found in edge node software, it is vital to distribute patches immediately. Without update notifications, microcontrollers run outdated, vulnerable firmware for years, providing easy entry points for network attacks.

## 2.7 Empirical Synthesis of Selected Literature (Thematic Comparative Matrix)
The following matrix synthesizes the features and limitations of 14 key studies in smart agricultural monitoring:

| Source Author & Year | System Core Stack | Real-time Alerting | Offline Buffer | Security Model | Gaps Identified |
|---|---|---|---|---|---|
| Abraham & Stephen (2025) | Arduino + GSM SMS | SMS Alerts (High Latency) | No | None | High operating SMS costs, no UI |
| Okello et al. (2025) | ESP32 + Blynk App | Blynk Push | No | Proprietary Blynk Token | No offline storage, data lost on Wi-Fi drop |
| Lengkong et al. (2025) | ESP8266 + HTTP API | Email (polling) | No | Static API Key | Vulnerable to key theft, high latency |
| Kale et al. (2024) | Raspberry Pi + Arduino | Web Server | No | Basic HTTP Auth | No cloud scalability, complex local wiring |
| Abdullah & Hamdan (2023) | ESP32 + MQTT | Dashboard View | No | None | No notification trigger, lacks secure auth |
| Shirse (2026) | ESP8266 + DHT22 | Local LED/Buzzer | No | None | No mobile app interface, lacks remote notifications |
| Gatkal et al. (2025) | Microcontrollers + WSN | Local Display | No | None | General agricultural review, no mobile app focus |
| Terence et al. (2024) | WSN + Cloud CPS | Web Dashboard | No | Basic SSL | Review paper, does not implement physical solution |
| Nalendra & Waspada (2025) | ESP32 + WebSockets | In-app alerts | No | Static token | No offline data storage, lacks background alert |
| Brindha et al. (2025) | AIoT + Cloud | Mobile Push | No | Basic HTTPS | Does not cover firmware version security updates |
| Sahoo & Pattnaik (2019) | Arduino + WSN | Local relay control | No | None | No cloud logging, lacks remote mobile HMI |
| Wolfert et al. (2017) | Big Data Framework | Cloud Dashboard | No | Standard SSL | Conceptual smart farming review, no edge implementation |
| Kamilaris et al. (2017) | Big Data Stack | Analysis Reports | No | None | Focuses on data mining rather than real-time edge control |
| Ray et al. (2017) | IoT Gateways | Basic Alerting | No | None | Early literature review, lacks secure transport details |
| **This Study (Egg Guardian)** | **ESP32 + FastAPI + Flutter** | **FCM Push + WebSocket + Gmail API** | **Yes (20 records)** | **JWT, TLS, Security Update Alerts** | *None (Focus of validation)* |

## 2.8 Identification of Research Gaps

### 2.8.1 The Isolation of Smart Environmental Architecture from Mobile App Security
In most smart farming literature, IoT system design and mobile application security are treated as separate concerns. Systems focus on temperature precision while leaving data channels unencrypted and access unauthenticated.

### 2.8.2 Absence of Low-Cost, Secure Storage Platforms for Developing Agricultural Economies
There is a lack of end-to-end, secure, open-source systems specifically designed to run on resource-constrained networks. The development of a secure, lightweight, and offline-resilient platform using standard frameworks like FastAPI and Flutter represents a clear contribution to the field.
