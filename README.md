# Supply Chain Optimization & Carrier Performance Diagnostics

## 📌 Executive Summary
This project features an interactive analytics architecture designed to audit and optimize carrier logistics across a North American distribution network. During the diagnostic phase, a **systemic network failure** was uncovered: 100% of active carriers fell significantly below the contractually mandated **90% Service Level Agreement (SLA)**. 

By implementing an end-to-end data pipeline powered by **SQL, Python, and Power BI**, alongside advanced data modeling and **AI orchestration**, this analysis isolated severe, localized logistics bottlenecks, moving the conversation from isolated carrier blame to structural warehouse optimization.

---

## 🏗️ System Architecture & Data Workflow
The pipeline utilizes an automated data architecture to ingest raw transactional data from warehouse enterprise systems, transform the metrics via an analytics layer, and serve interactive visual intelligence to executive decision-makers.

+------------------------------+     +----------------------------+     +----------------------------+
|     Data Ingestion Layer     |     |    Transformation Layer    |     |  Executive Insights Layer  |
|          (SQL & Python)      |     |         (Power BI)         |     |        (Power BI / AI)     |
|                              |     |                            |     |                            |
| * Extract Trans Logs (SQL)   | --> | * ETL & Schema Cleansing   | --> | * Analytics Reference      |
| * Preprocessing & Clean      |     | * DAX Metric Modeling      |     |   Baselines (50% / 90%)    |
|   Anomalies (Python)         |     | * Conditional Formatter    |     | * Dynamic Root Cause       |
+------------------------------+     +----------------------------+     |   Fulfillment Alerting     |
                                                                        +----------------------------+
---

## 🌊 Technical Workflow & Operational Overflow
When raw delivery files cross operational boundaries, the processing engine checks network stability through a cascading logic workflow across our tech stack:

1. **Ingestion & Validation (SQL & Python):** Structured logs are queried via **SQL** and fed into a **Python** script to clean formatting inconsistencies and handle missing timestamps.
2. **Analytics Aggregation (Power BI):** The Power BI engine consumes the processed dataset to calculate the actual on-time performance against active shipment volume using custom DAX measures.
3. **SLA Evaluation Gateway:** 
   * **If performance ≥ 90%:** Lane marked as *Optimal / Compliant* (Green).
   * **If 50% ≤ performance < 90%:** Lane marked as *At Risk / Underperforming* (Slate Blue).
   * **If performance < 50%:** System triggers the **Operational Overflow Condition** (Crimson Red alert). This forces a structural pivot from carrier transport auditing to internal warehouse cross-dock diagnostic verification.

---
## 🛠️ Technology Stack & Implementations

### 1. SQL (Data Extraction & Structuring)
*   Engineered optimized relational queries to pull complex transaction tables, joining carrier dispatch timestamps with warehouse inventory logs.
*   Aggregated high-volume transit records down to key performance intervals to reduce processing latency in downstream BI layers.

### 2. Python (Data Cleansing & Diagnostics)
*   Utilized libraries like `pandas` and `numpy` to isolate missing shipping records and normalize date-time fields across disparate carrier reporting formats.
*   Conducted outlier testing to verify that the statistical grouping of poor-performing carriers was mathematically uniform.

### 3. Power BI (Visual Intelligence & DAX modeling)
*   **Dynamic Conditional Formatting (DAX):** Rather than hardcoding static visual elements, a dynamic color measure was implemented to automatically audit performance against the historical floor. If a carrier falls beneath the 50% threshold, the dashboard dynamically alerts the user:
    ```dax
    Carrier Color Formatting = 
    VAR CurrentPerformance = [On_Time_Delivery_Rate]
    RETURN
        IF(
            CurrentPerformance < 0.50, 
            "#B91C1C", -- Crimson Red alert for sub-floor performance
            "#475569"  -- Slate Blue for baseline-viable carriers
        )
    ```
*   **Multi-Tiered Analytics Reference Lines:** Plotted a primary SLA Line (90% dashed line) illustrating the contractual target, and a Historical Floor Line (50% dotted line) to differentiate macro gridlock from isolated carrier negligence.

### 4. AI Co-Pilot Integration (Development Efficiency)
To optimize development velocity and ensure enterprise-grade formatting, an Advanced AI LLM was utilized as a technical and strategic co-pilot throughout this project lifecycle across three specific pillars:
*   **DAX & Script Optimization:** Accelerated the engineering of conditional logic and verified Python preprocessing efficiency.
*   **Data Modeling Diagnostics:** Partnered with AI to evaluate the ~40% carrier cluster, identifying the mathematical likelihood of an internal origin-warehouse bottleneck rather than random distribution errors.
*   **Strategic Narrative Framing:** Translated technical dashboard data points into professional, boardroom-ready supply chain terminology—directly mirroring the KPIs used by enterprise logistics managers.

---

## 📊 Core Operational Metrics Uncovered
A deep dive into carrier delivery success rates revealed a stark divide across the logistics network:

*   **Contractual Target:** 90.0% SLA Delivery Rate
*   **Historical Network Floor:** 50.0% Delivery Rate
*   **Carrier Alpha (Top Performer):** **63.1%** *(Cleared the historical floor; isolated as operationally viable)*
*   **Carrier Cluster Beta, Gamma, Delta:** **40.8%, 39.8%, 39.5%** *(Critical failure zone below the network floor)*

---

## 🔍 Critical Diagnostic Insights (The Interview Narrative)
When evaluating the data, two critical operational conclusions were delivered to leadership:

1.  **The Outlier Evaluation:** Carrier Alpha achieved a **63.1% on-time rate**. While still technically failing the 90% SLA, clearing the 50% historical floor proves that their specific regional hub remained functional under pressure, making them a prime candidate for temporary lane expansion.
2.  **The Systemic Warehouse Bottleneck:** The remaining three independent carriers completely flatlined, clustering tightly within **1.3%** of each other (~40%). Because multiple independent operators failed at the exact same statistical rate, it indicates that the crisis was **not a carrier transport issue**, but rather an internal origin warehouse bottleneck (e.g., severe fulfillment delays at the main shipping docks) freezing out the network.

---

## 📈 Strategic Recommendations & Next Steps
Based on the dashboard analytics, the following immediate actions were recommended to the operations team:
*   **Shift Volume to Top Performer:** Immediately divert high-priority shipping lanes to Carrier Alpha (63.1%) to stabilize immediate delivery disruptions.
*   **Conduct Internal Cross-Dock Audit:** Initiate an immediate audit of the origin facility's loading docks, as the tightly clustered 40% failure rates point directly to internal cross-docking friction rather than transit delays.
*   **Renegotiate Contractual Baselines:** Utilize this dashboard's historical data to renegotiate realistic SLA tiers during peak seasonal volatility or macro network gridlocks.
