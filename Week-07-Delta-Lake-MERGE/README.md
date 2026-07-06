# 🔺 Week-07-Delta-Lake-MERGE

### Delta Lake MERGE Implementation | Celebal Technologies Excellence Internship (CEI)

![Platform](https://img.shields.io/badge/Platform-Databricks%20Free%20Edition-red)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Framework](https://img.shields.io/badge/Framework-PySpark-orange)
![Storage](https://img.shields.io/badge/Storage-Delta%20Lake-brightgreen)
![Catalog](https://img.shields.io/badge/Catalog-Unity%20Catalog-lightgrey)

---

## 📌 Project Overview

This repository contains my **Week 07** submission for the **Celebal Technologies Excellence Internship (CEI)**. The project demonstrates **incremental data processing using Delta Lake**, implemented on **Databricks Free Edition (Unity Catalog)** using **PySpark**.

The workflow covers loading raw data into a Delta Table, cleaning it, generating an incremental dataset, and applying **Delta Lake `MERGE`** operations to update existing records and insert new ones — a core pattern in real-world incremental data engineering pipelines.

---

## 🎯 Objective

Perform incremental data processing using Delta Lake by implementing `MERGE` operations in Databricks. The project demonstrates loading data into Delta Tables, cleaning data, creating incremental datasets, applying `MERGE` operations, validating results, and understanding incremental data engineering workflows.

---

## ✨ Features

- ✅ Managed Delta Table creation in Unity Catalog
- ✅ Data exploration and schema inspection
- ✅ Missing value checks
- ✅ Duplicate record removal
- ✅ Incremental dataset creation
- ✅ Delta Lake `MERGE INTO` implementation (Update + Insert)
- ✅ Post-merge validation (row count & duplicate checks)
- ✅ Final Delta Table display

---

## 🛠️ Technologies Used

| Category | Tools / Tech |
|---|---|
| Platform | Databricks Free Edition (Unity Catalog) |
| Language | Python |
| Framework | PySpark |
| Storage Layer | Delta Lake |
| Compute Engine | Apache Spark |
| Data Governance | Unity Catalog |

---

## 📁 Folder Structure

```
Week-07-Delta-Lake-MERGE/
├── data/
│   ├── sample_superstore.csv
│   └── sample_superstore_incremental.csv
├── notebooks/
│   └── delta_scd_assignment.ipynb
├── screenshots/
├── README.md
└── requirements.txt
```

---

## 🔄 Workflow Diagram

```
┌─────────────────────┐
│  Load Superstore CSV │
└──────────┬───────────┘
           ▼
┌─────────────────────────┐
│ Create Managed Delta     │
│ Table (sample_superstore │
│ _data)                   │
└──────────┬───────────────┘
           ▼
┌─────────────────────────┐
│ Load into Spark DataFrame│
└──────────┬───────────────┘
           ▼
┌─────────────────────────┐
│ Explore & Check Missing  │
│ Values                   │
└──────────┬───────────────┘
           ▼
┌─────────────────────────┐
│ Remove Duplicate Records │
└──────────┬───────────────┘
           ▼
┌─────────────────────────┐
│ Create Incremental       │
│ Dataset                  │
└──────────┬───────────────┘
           ▼
┌─────────────────────────┐
│ Apply Delta Lake MERGE   │
│ (Update + Insert)        │
└──────────┬───────────────┘
           ▼
┌─────────────────────────┐
│ Validate Row Count &     │
│ Duplicates               │
└──────────┬───────────────┘
           ▼
┌─────────────────────────┐
│ Display Final Delta Table│
└─────────────────────────┘
```

---

## 🧩 Project Steps Implemented

1. **Load dataset into Delta Table**
2. **Perform data cleaning**
   - Handle missing values
   - Remove duplicate records
3. **Create Incremental Dataset**
4. **Perform MERGE**
   - Update Existing Records
   - Insert New Records
5. **Validate Results**
   - Row Count
   - Duplicate Validation
6. **Display Final Dataset**

---

## ✅ Work Completed

- ✔ Uploaded the Superstore dataset into Databricks
- ✔ Created a Managed Delta Table named `sample_superstore_data`
- ✔ Loaded the Delta Table into a Spark DataFrame
- ✔ Explored the dataset
- ✔ Checked missing values
- ✔ Removed duplicate records
- ✔ Created an Incremental Dataset
- ✔ Applied Delta Lake MERGE
- ✔ Updated existing records
- ✔ Inserted new records
- ✔ Validated row count
- ✔ Validated duplicate records
- ✔ Displayed the final Delta Table

---

## 📊 Datasets

| Dataset | Description |
|---|---|
| `sample_superstore.csv` | Original dataset loaded into the Delta Table |
| `sample_superstore_incremental.csv` | Incremental dataset used for the MERGE operation |

---

## 🖼️ Screenshots

All screenshots documenting the workflow are available in the [`screenshots/`](./screenshots) folder:

| # | Screenshot | Description |
|---|---|---|
| 01 | `01_delta_table_created.png` | Delta Table creation |
| 02 | `02_dataset_loaded.png` | Dataset loaded into DataFrame |
| 03 | `03_schema_information.png` | Schema information |
| 04 | `04_dataset_statistics.png` | Dataset statistics |
| 05 | `05_missing_values_check.png` | Missing values check |
| 06 | `06_cleaned_dataset.png` | Cleaned dataset |
| 07 | `07_incremental_dataset_created.png` | Incremental dataset created |
| 08 | `08_delta_merge_operation.png` | Delta MERGE operation |
| 09 | `09_final_row_count.png` | Final row count validation |
| 10 | `10_duplicate_validation.png` | Duplicate validation |
| 11 | `11_final_delta_table.png` | Final Delta Table |

---

## ⚠️ Challenges Faced

**Challenge 1: DBFS Root Restrictions**
Databricks Free Edition uses **Unity Catalog**, which disables the **Public DBFS Root**. As a result, exporting Delta Tables directly as CSV using DBFS was not possible.

**Challenge 2: `UC_VOLUME_NOT_FOUND` Error**
While attempting to export the cleaned Delta table, the following error occurred:

```
UC_VOLUME_NOT_FOUND
```

This happened because no **Unity Catalog Volume** had been created to serve as an export destination.

**Challenge 3: Limited Export of Managed Tables**
Since Databricks Free Edition restricts direct export of managed Delta Tables, this repository contains only the **original** and **incremental** datasets, while the **cleaned and merged data** is demonstrated completely inside the notebook.

> **Note:** These challenges are **platform limitations of Databricks Free Edition**, not implementation errors. All cleaning, MERGE, and validation logic was successfully implemented and executed, as shown in the notebook and screenshots.

---

## 📚 Learning Outcomes

Through this assignment, I gained hands-on experience with:

- Databricks environment and workflow
- Apache Spark fundamentals
- PySpark DataFrame operations
- Delta Lake architecture
- Creating and managing Delta Tables
- `MERGE INTO` syntax and semantics
- Incremental data processing patterns
- Data validation techniques
- Updating existing records via MERGE
- Inserting new records via MERGE
- Working with Managed Delta Tables in Unity Catalog

---

## 🚀 Future Improvements

- 🏗️ Implement Bronze-Silver-Gold Architecture
- 🔁 Build Automated Incremental Pipelines
- 🌊 Explore Streaming Data Processing
- ⚡ Adopt Delta Live Tables
- ☁️ Integrate with Azure Data Factory
- ⏰ Schedule pipelines using Databricks Workflows

---

## 👤 Author

**Dev Charaya**
MCA (Data Science & Analytics)
JECRC University, Jaipur
Celebal Technologies Excellence Intern
Aspiring Data Engineer

🔗 GitHub: [@charayadev](https://github.com/charayadev)

---

## 🙏 Acknowledgements

Thanks to **Celebal Technologies** for the opportunity to work on this **Excellence Internship** program and for providing a platform to learn real-world Data Engineering practices using Databricks and Delta Lake.

---

## 📄 License

This project is created for educational purposes as part of the **Celebal Technologies Excellence Internship**.