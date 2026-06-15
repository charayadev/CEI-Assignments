# 🏪 Azure Retail Analytics — Medallion Architecture with ADF

![Azure](https://img.shields.io/badge/Azure-Data%20Factory-0089D6?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Storage](https://img.shields.io/badge/Azure-Blob%20Storage-0089D6?style=for-the-badge&logo=microsoftazure&logoColor=white)
![Architecture](https://img.shields.io/badge/Architecture-Medallion-FFD700?style=for-the-badge)
![Status](https://img.shields.io/badge/Pipeline-Succeeded%20✅-28A745?style=for-the-badge)
![IAM](https://img.shields.io/badge/IAM-RBAC%20Configured-DC3545?style=for-the-badge)

> **End-to-end cloud data pipeline** built on Microsoft Azure — ingesting raw retail data through a structured Bronze → Silver → Gold Medallion Architecture using Azure Data Factory, enabling scalable analytics and future Power BI reporting.

---

## 📋 Project Overview

This project demonstrates a production-grade **ETL pipeline** for retail analytics on Azure. Raw transactional data (Sample Superstore) is ingested into cloud storage, validated, transformed, and promoted through a tiered data lake architecture — following the **Medallion Architecture** pattern widely adopted in modern data engineering.

The pipeline is fully orchestrated via **Azure Data Factory (ADF)** with IAM role-based access control, making it secure, auditable, and enterprise-ready.

---

## 💼 Business Problem

Retail organizations generate high-volume transactional data that often sits in siloed, unstructured formats — making it difficult to derive timely business insights. Without a structured ingestion and transformation layer, data quality issues propagate downstream into analytics and reporting.

**This solution addresses:**
- Lack of a governed, layered data storage strategy
- No separation between raw, cleansed, and analytics-ready data
- Absence of automated pipeline orchestration and monitoring

---

## 🏗️ Solution Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     Azure Data Lake (Blob Storage)              │
│                                                                 │
│  [Raw CSV Input]                                                │
│       │                                                         │
│       ▼                                                         │
│  ┌──────────┐    ┌──────────────────┐    ┌──────────────────┐  │
│  │  BRONZE  │───▶│  Get Metadata    │───▶│  Copy Data       │  │
│  │  Layer   │    │  Activity (ADF)  │    │  Activity (ADF)  │  │
│  └──────────┘    └──────────────────┘    └────────┬─────────┘  │
│                                                   │             │
│                                          ┌────────▼─────────┐  │
│                                          │  SILVER Layer    │  │
│                                          │  (Cleansed CSV)  │  │
│                                          └────────┬─────────┘  │
│                                                   │             │
│                                          ┌────────▼─────────┐  │
│                                          │  GOLD Layer      │  │
│                                          │  (Future: Agg.)  │  │
│                                          └────────┬─────────┘  │
│                                                   │             │
│                                          ┌────────▼─────────┐  │
│                                          │  Power BI        │  │
│                                          │  (Future)        │  │
│                                          └──────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🖼️ Architecture Diagram

> 📸 *Architecture diagram and pipeline screenshots are available in the [`images/`](./images/) folder.*

| # | Screenshot | Description |
|---|---|---|
| 01 | `images/01_Resource_Group_Creation.png` | Azure Resource Group provisioned for the project |
| 02 | `images/02_Storage_Account_Creation.png` | Storage Account `stretailanalyticsdev01` configured |
| 03 | `images/03_Medallion_Containers_Bronze_Silver_Gold.png` | Bronze, Silver, and Gold containers created |
| 04 | `images/04_Bronze_Layer_Dataset_Upload.png` | `Sample-Superstore.csv` uploaded to Bronze container |
| 05 | `images/05_Dataset_Metadata_and_Properties.png` | Dataset metadata and schema properties |
| 06 | `images/06_Azure_Data_Factory_Creation.png` | ADF instance `adf-retail-analytics-dev` provisioned |
| 07 | `images/07_ADF_Studio_Overview.png` | Azure Data Factory Studio landing view |
| 08 | `images/08_Linked_Service_Configuration.png` | `LS_AzureStorage_RetailAnalytics` linked service setup |
| 09 | `images/09_Linked_Service_Test_Connection_Success.png` | Linked Service connection test — Succeeded |
| 10 | `images/10_Source_Dataset_Bronze_Layer.png` | `DS_Bronze_Superstore` source dataset configuration |
| 11 | `images/11_Destination_Dataset_Silver_Layer.png` | `DS_Silver_Superstore` destination dataset configuration |
| 12 | `images/12_Get_Metadata_Activity.png` | Get Metadata Activity configured in pipeline |
| 13 | `images/13_Pipeline_Design_Bronze_To_Silver.png` | `PL_Bronze_To_Silver` pipeline canvas design |
| 14 | `images/14_ADF_Pipeline_Published.png` | Pipeline published successfully to ADF |
| 15 | `images/15_Pipeline_Debug_Success.png` | Pipeline debug run — all activities Succeeded |
| 16 | `images/16_Monitor_Pipeline_Runs.png` | ADF Monitor view showing pipeline run history |
| 17 | `images/17_Silver_Output_File.png` | `superstore_cleaned.csv` landed in Silver container |
| 18 | `images/18_IAM_Role_Assignments.png` | RBAC role assignments on the resource group |
| 19 | `images/19_Medallion_Architecture.png` | End-to-end Medallion Architecture diagram |
| 20 | `images/20_Final_Resource_Group_Resources.png` | Final state of all Azure resources deployed |

---

## 🛠️ Technologies Used

| Category | Tool / Service |
|---|---|
| Cloud Platform | Microsoft Azure |
| Orchestration | Azure Data Factory (ADF) |
| Storage | Azure Blob Storage (Data Lake) |
| Data Format | CSV (Superstore retail dataset) |
| Access Control | Azure IAM (RBAC) |
| Future Reporting | Power BI |

---

## ☁️ Azure Resources

| Resource | Name |
|---|---|
| Resource Group | `rg-retail-analytics-dev` |
| Storage Account | `stretailanalyticsdev01` |
| Data Factory | `adf-retail-analytics-dev` |
| Containers | `bronze`, `silver`, `gold` |

---

## 🥉🥈🥇 Medallion Architecture

The Medallion Architecture organizes data into three progressive quality layers:

| Layer | Container | Purpose | Dataset |
|---|---|---|---|
| **Bronze** | `bronze/` | Raw ingestion — no transformations, source of truth | `Sample-Superstore.csv` |
| **Silver** | `silver/` | Cleansed, validated, and standardized data | `superstore_cleaned.csv` |
| **Gold** | `gold/` | Aggregated, analytics-ready data *(future)* | TBD |

This approach ensures **data lineage**, **reprocessing capability**, and **clear separation of concerns** across the data lifecycle.

---

## 🔄 Data Pipeline Workflow

```
Sample-Superstore.csv
        │
        ▼
  Bronze Container          ← Raw file landed via manual/ADF ingestion
        │
        ▼
  Get Metadata Activity     ← Validates file existence and properties
        │
        ▼
  Copy Data Activity        ← Reads from Bronze, writes to Silver
        │
        ▼
  Silver Container          ← Cleansed output: superstore_cleaned.csv
        │
        ▼
  Gold Layer (Planned)      ← Aggregations & business metrics
        │
        ▼
  Power BI (Planned)        ← Self-service dashboards & reporting
```

---

## ⚙️ Azure Data Factory Components

**Linked Service**
- `LS_AzureStorage_RetailAnalytics` — Connects ADF to the Azure Blob Storage account using secure credentials.

**Datasets**
- `DS_Bronze_Superstore` — Points to `Sample-Superstore.csv` in the Bronze container.
- `DS_Silver_Superstore` — Points to `superstore_cleaned.csv` in the Silver container.

**Pipeline**
- `PL_Bronze_To_Silver` — Orchestrates the full Bronze-to-Silver promotion workflow.

**Activities**

| Activity | Type | Purpose |
|---|---|---|
| Get Metadata | Metadata | Validates source file exists before processing |
| Copy Data | Copy | Transfers and lands data from Bronze to Silver |

---

## 📁 Project Folder Structure

```
Week-04-azure-retail-analytics-medallion-adf/
│
├── images/                         # Pipeline & resource screenshots
│   ├── resource-group.png
│   ├── storage-account.png
│   ├── containers.png
│   ├── linked-service.png
│   ├── bronze-dataset.png
│   ├── silver-dataset.png
│   ├── pipeline-design.png
│   ├── pipeline-success.png
│   ├── pipeline-monitoring.png
│   ├── iam-config.png
│   ├── silver-output.png
│   └── architecture-diagram.png
│
├── dataset/                        # Source and output datasets
│   ├── Sample-Superstore.csv
│   └── superstore_cleaned.csv
│
└── README.md
```

---

## ✅ Pipeline Execution Results

| Run | Pipeline | Status | Trigger |
|---|---|---|---|
| 1 | `PL_Bronze_To_Silver` | ✅ Succeeded | Manual |

The pipeline executed without errors. The `Get Metadata` activity successfully validated the source file, and the `Copy Data` activity promoted the dataset from the Bronze container to the Silver container as `superstore_cleaned.csv`.

> 📸 See `images/15_Pipeline_Debug_Success.png` and `images/16_Monitor_Pipeline_Runs.png` for ADF Monitor screenshots.

---

## 🔐 IAM Roles Configured

| Role | Scope | Purpose |
|---|---|---|
| Owner | Resource Group | Full administrative control |
| Reader | Storage Account | Read-only access for auditing |
| Storage Blob Data Contributor | Containers | ADF read/write access to Blob Storage |

---

## 📚 Key Learnings

- Designed and deployed a **cloud-native data lake** using Azure Blob Storage with a tiered container strategy.
- Built and configured **ADF Linked Services, Datasets, and Pipelines** from scratch without pre-built templates.
- Applied the **Medallion Architecture** pattern to enforce data quality boundaries between raw, cleansed, and curated zones.
- Implemented **Azure RBAC** using the principle of least privilege for secure resource access.
- Used **Get Metadata Activity** as a pre-flight check to make pipelines resilient to missing source files.

---

## 🚀 Future Improvements

- [ ] **Gold Layer Transformation** — Add ADF Data Flow or Databricks notebooks for business-level aggregations (sales by region, category profitability).
- [ ] **Parameterized Pipelines** — Refactor using pipeline parameters and variables for dynamic file paths.
- [ ] **Trigger Automation** — Schedule pipelines using ADF tumbling window or storage event triggers.
- [ ] **Data Quality Checks** — Integrate Azure Purview or custom validation activities for schema enforcement.
- [ ] **Power BI Integration** — Connect the Gold layer to Power BI for self-service retail analytics dashboards.
- [ ] **CI/CD with Azure DevOps** — Automate ADF deployment using ARM templates and Git integration.

---

## 🧠 Skills Demonstrated

`Azure Data Factory` · `Azure Blob Storage` · `Medallion Architecture` · `ETL Pipeline Design` · `Data Lake Architecture` · `Azure IAM / RBAC` · `Cloud Data Engineering` · `Pipeline Monitoring` · `CSV Data Processing`

---

## 👤 Author

**[Your Name]**
*Data Engineer | Azure | Python | SQL*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/your-profile)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat&logo=github)](https://github.com/your-username)

---

> 💡 *Part of an ongoing Azure Data Engineering portfolio. Each project builds progressively toward production-grade cloud architectures.*
