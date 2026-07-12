# 🛒 Procurement & Vendor Spend Analytics Pipeline

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-3.x-E25A1C?logo=apachespark&logoColor=white)
![Delta Lake](https://img.shields.io/badge/Delta%20Lake-Enabled-00ADD8?logo=delta&logoColor=white)
![Databricks](https://img.shields.io/badge/Databricks-Lakehouse-FF3621?logo=databricks&logoColor=white)
![Unity Catalog](https://img.shields.io/badge/Unity%20Catalog-Governed-6E56CF)
![ADLS Gen2](https://img.shields.io/badge/Azure-ADLS%20Gen2-0089D6?logo=microsoftazure&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A production-style **Data Engineering Lakehouse pipeline** that transforms raw synthetic procurement data into clean, validated, business-ready analytics using the **Medallion Architecture** (Bronze → Silver → Gold) on **Databricks** with **Delta Lake** and **Unity Catalog**.

---

## 📌 Project Overview

This project simulates an end-to-end enterprise **Procurement & Vendor Spend Analytics** pipeline. It generates realistic (and intentionally messy) procurement data, then progressively cleans, standardizes, and models it through Bronze, Silver, and Gold layers — culminating in SQL-driven business analytics and an automated data validation report.

---

## 🏗️ Architecture Diagram

```
        ┌───────────────────────────┐
        │  Python Data Generation   │
        └────────────┬──────────────┘
                     │
        ┌────────────▼──────────────┐
        │        Bronze Layer       │
        │   (Raw Ingested Data)     │
        └────────────┬──────────────┘
                     │
        ┌────────────▼──────────────┐
        │        Silver Layer       │
        │ (Cleaned, SCD Type 2)     │
        └────────────┬──────────────┘
                     │
        ┌────────────▼──────────────┐
        │         Gold Layer        │
        │  (Business Aggregates)    │
        └────────────┬──────────────┘
                     │
        ┌────────────▼──────────────┐
        │       SQL Analytics       │
        └────────────────────────────┘
```

---

## 🧰 Technology Stack

| Category | Tools |
|---|---|
| Language | Python |
| Processing | PySpark, Spark SQL |
| Storage Format | Delta Lake |
| Platform | Databricks |
| Governance | Unity Catalog |
| Cloud Storage | Azure Data Lake Storage Gen2 (ADLS Gen2) |
| Version Control | Git, GitHub |

---

## 📁 Folder Structure

```
procurement-vendor-analytics-pipeline/
│
├── data/
│   ├── raw/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── notebooks/
│   ├── 01_Data_Generation/
│   │      Data_Generation.py
│   │
│   ├── 02_Bronze/
│   │      Bronze_ETL.ipynb
│   │
│   ├── 03_Silver/
│   │      Silver_ETL_With_SCD2.ipynb
│   │
│   ├── 05_Gold/
│   │      GOLD_ETL.ipynb
│   │
│   └── 06_Data_Validation/
│          Data_Validation_Report.ipynb
│
├── sql/
│      SQL_Analytics.ipynb
│
├── screenshots/
│
├── documentation/
│      Procurement_Vendor_Spend_Analytics_Pipeline_Documentation.docx
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

## 🔄 Workflow

1. **Generate** synthetic procurement and vendor data (including intentional data quality issues).
2. **Ingest** raw data into the **Bronze layer** with minimal transformation.
3. **Clean and standardize** data in the **Silver layer**, applying statistical imputation, outlier detection, and **SCD Type 2** history tracking.
4. **Aggregate** business-ready datasets in the **Gold layer**.
5. **Analyze** vendor spend and procurement trends using **SQL Analytics**.
6. **Validate** the entire pipeline with an automated **Data Validation Report**.

---

## ✨ Project Features

- ✔ Synthetic Procurement Data Generation
- ✔ Bronze Layer Ingestion
- ✔ Silver Layer Cleansing
- ✔ Statistical Data Cleaning (Mean, Median, Mode)
- ✔ Duplicate Handling
- ✔ Data Standardization
- ✔ IQR Outlier Detection
- ✔ SCD Type 2 using Delta Lake MERGE
- ✔ Gold Layer Aggregation
- ✔ SQL Analytics
- ✔ Data Validation Report

---

## 🗃️ Dataset Description

The dataset is **synthetically generated** to mimic a real-world procurement system, including vendors, purchase orders, invoices, and spend categories. Intentional data quality issues (nulls, duplicates, inconsistent formatting, and outliers) are injected to simulate realistic enterprise data conditions.

---

## 🥉 Bronze Layer

Raw synthetic data is ingested as-is into Delta tables, preserving the original structure and values for full traceability and reprocessing capability.

## 🥈 Silver Layer

The Silver layer applies:
- **Statistical missing value handling** using mean, median, and mode imputation strategies
- **Duplicate record removal**
- **Standardization** of formats, casing, and categorical values

### 📊 IQR Outlier Detection

Numerical fields (such as spend amounts and quantities) are evaluated using the **Interquartile Range (IQR)** method to flag and handle statistical outliers.

### 🔁 SCD Type 2

Vendor and procurement dimension changes are tracked historically using **Slowly Changing Dimension Type 2**, implemented via **Delta Lake `MERGE`** operations to preserve full change history.

## 🥇 Gold Layer

Cleaned and historized Silver data is aggregated into business-ready Gold tables optimized for reporting and analytics consumption.

## 🧮 SQL Analytics

Curated SQL queries run against the Gold layer to surface vendor spend trends, procurement patterns, and category-level insights.

## ✅ Data Validation

An automated **Data Validation Report** checks row counts, null rates, duplicate rates, and schema integrity across all layers to ensure pipeline reliability.

---

## 🛠️ Engineering Enhancements

- Professional synthetic data generation
- Intentional bad data generation (for realistic cleaning scenarios)
- Statistical missing value handling
- IQR Outlier Detection
- SCD Type 2 using Delta MERGE
- Business Validation
- SQL Analytics
- Data Validation Report

---

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/charayadev/procurement-vendor-analytics-pipeline.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Upload the `notebooks/` folder to your **Databricks workspace**.
4. Configure **Unity Catalog** and **ADLS Gen2** storage credentials.
5. Run notebooks sequentially:
   - `01_Data_Generation` → `02_Bronze` → `03_Silver` → `05_Gold` → `06_Data_Validation`
6. Execute `sql/SQL_Analytics.ipynb` for business insights.

---

## 📤 Project Output

- Cleaned, validated, and historized Delta tables across Bronze, Silver, and Gold layers
- Business-ready vendor spend analytics
- Automated data validation report confirming pipeline data quality

---

## 🎓 Learning Outcomes

- Designing and implementing a Medallion Architecture Lakehouse pipeline
- Applying statistical data cleaning techniques at scale with PySpark
- Implementing SCD Type 2 using Delta Lake MERGE
- Performing outlier detection using the IQR method
- Governing data with Unity Catalog on Databricks
- Writing business-focused SQL analytics on curated Gold data

---

## 🚀 Future Improvements

- Workflow orchestration with Databricks Jobs / Workflows
- CI/CD integration for automated testing and deployment
- Expanded data quality framework with configurable rule sets
- Additional Gold-layer marts for procurement forecasting

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Name:** Dev Charaya
**Role:** MCA (Data Science & Analytics) Student | Aspiring Data Engineer

**Internship:** This project was developed as part of the **Celebal Technologies Data Engineering Internship Program**.

It demonstrates practical, hands-on implementation of:

- Python
- PySpark
- Databricks
- Delta Lake
- Spark SQL
- Medallion Architecture
- Data Engineering Best Practices

---

## 📬 Connect with Me

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:charayadev11@gmail.com
)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dev-charaya21/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/charayadev)



---

⭐ If you found this project useful, consider giving this repository a star.

Thank you for visiting this repository. Feedback and suggestions are always welcome.

Made with ❤️ by **Dev Charaya**.