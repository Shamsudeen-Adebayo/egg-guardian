# CHAPTER 5: SUMMARY, CONCLUSION, & RECOMMENDATIONS

## 5.1 Summary of Findings
This study designed, implemented, and evaluated the Egg Guardian system—a secure, real-time cyber-physical monitoring solution for poultry egg storage and temperature regulation. The findings from the empirical evaluations in Chapter 4 are summarized as follows:
*   **Sensor Accuracy & Calibration**: Calibration of the DS18B20 digital sensor against a mercury reference thermometer yielded a **Mean Absolute Error (MAE) of $0.24^\circ\text{C}$**, which is well within the acceptable $\pm 0.5^\circ\text{C}$ threshold required for poultry egg incubation (Trust, 2026).
*   **Telemetry Latency**: End-to-end data propagation latency averaged **$1.14\text{ seconds}$** over a local farm Wi-Fi network and **$1.41\text{ seconds}$** over a mobile 4G link. This meets the real-time operational delivery requirements (Nalendra & Waspada, 2025).
*   **Edge Resiliency & Recovery**: The local FIFO caching buffer on the ESP32 achieved a **100% data recovery rate** for simulated network dropouts lasting up to 100 seconds (Pacheco da Costa et al., 2023). Under longer outages, the ring buffer correctly overwrote the oldest telemetry points first, preserving the 20 most recent readings.
*   **Security Update Warnings**: The system verified firmware versions in $120\text{ms}$. When a version mismatch was detected, the backend successfully triggered warning badges in the mobile app and sent notifications via FCM (Dr. Brindha S et al., 2025).
*   **System Usability**: Field testing with 10 poultry operators using the System Usability Scale (SUS) yielded an average usability score of **$77.5 / 100$**, corresponding to "excellent" usability (Adebayo, 2022).

---

## 5.2 Final Conclusion
The Egg Guardian project demonstrates that low-cost, off-the-shelf microcontrollers (such as the ESP32) can manage poultry egg storage climates when paired with modern asynchronous protocols (MQTTS, WebSockets) and local caching queues (Protopappas et al., 2025). The system maintains telemetry accuracy and alerts operators to biological temperature boundary violations ($37.0^\circ\text{C}$ to $39.0^\circ\text{C}$) (FAO, 2024). Additionally, the version check handshake protects the edge network against outdated firmware vulnerabilities. In conclusion, the system provides a secure, reliable, and cost-effective monitoring solution for smart agricultural applications.

---

## 5.3 Practical and Commercial Implementation Issues
Deploying the system in commercial poultry hatcheries presents several practical challenges:
*   **Environmental Protection**: Hatcheries are high-humidity, dust-prone environments. The ESP32 edge node must be mounted inside an IP66-rated casing, and the DS18B20 temperature probe must be housed in a waterproof stainless-steel sheath to prevent moisture damage and short circuits.
*   **Network Range Constraints**: Metallic structures and thick concrete walls in commercial farms block Wi-Fi signals. Deploying the system across large facilities requires physical Wi-Fi repeaters or range extenders to ensure reliable connectivity.
*   **Power Redundancy**: Commercial operations require continuous monitoring. The edge nodes should be integrated with an Uninterruptible Power Supply (UPS) or backup batteries to maintain operations during power outages.

---

## 5.4 Research Contributions to Agricultural Computing
This study contributes to the field of smart farming in two main areas:
*   **Data Integrity on the Edge**: The study demonstrates that local caching queues allow low-cost microcontrollers to maintain data integrity during network drops (Pacheco da Costa et al., 2023). This reduces the need for expensive, high-RAM gateway hardware.
*   **Firmware Security Lifecycle Integration**: The study integrates security update alerts directly into the agricultural monitoring loop (Dr. Brindha S et al., 2025). This addresses a common vulnerability in IoT deployments, where microcontrollers are left running outdated, insecure firmware.

---

## 5.5 Project Limitations
The current implementation has three main limitations:
*   **Wi-Fi Dependency**: The ESP32 is restricted to 2.4GHz Wi-Fi. This limits system deployment in remote rural farms that lack local area network infrastructure.
*   **Memory Constraints**: Due to the ESP32's limited RAM, the local ring buffer holds a maximum of 20 telemetry records. During outages longer than 100 seconds, the buffer begins overwriting historical data.
*   **FCM Gateway Dependency**: The mobile notification system relies on Google's Firebase Cloud Messaging gateway. If Google services are offline or blocked, system tray alert notifications will fail to deliver.

---

## 5.6 Recommendations for Future Research
To build on this work, we recommend three directions for future research:
1.  **LoRaWAN Integration**: Replacing Wi-Fi with LoRaWAN to allow long-distance transmission (up to 15 km) in remote areas without internet access.
2.  **Predictive Thermal Analysis**: Deploying machine learning models (such as LSTM networks) on the backend server to analyze temperature trends and forecast heating/cooling failures before they occur.
3.  **Self-Healing OTA Updates**: Upgrading the update system from a warning banner to an automated Over-the-Air (OTA) patching pipeline that automatically updates the edge microcontroller when a version mismatch is detected.

Figure 5.1 illustrates the future research roadmap:

![Figure 5.1: Technical Future Research Roadmap block diagram, showing LoRaWAN gateways, LSTM predictive analysis, and secure self-healing OTA updates loops.]C:/Users/USER/.gemini/antigravity/brain/6500ed53-115c-4abd-abcb-3c1580976dd6/future_research_roadmap_1783896624272.png

---

## 5.7 Summary
This chapter summarized the findings of the Egg Guardian system, presented conclusions, and discussed practical implementation challenges, research contributions, and limitations. Finally, it recommended future research paths, including LoRaWAN integration, predictive machine learning, and self-healing OTA updates.
