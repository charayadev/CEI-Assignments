<div align="center">

# ⚡ Apache Spark – Data Cleaning, Transformation & Aggregation using DataFrames

### Week-05 | Data Engineer Internship | Celebal Technologies

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PySpark](https://img.shields.io/badge/Apache%20Spark-PySpark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)](https://spark.apache.org/)
[![Java](https://img.shields.io/badge/Java-17%20LTS-007396?style=for-the-badge&logo=openjdk&logoColor=white)](https://adoptium.net/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![VS Code](https://img.shields.io/badge/VS%20Code-Editor-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)](https://code.visualstudio.com/)
[![License](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)](#)

**Author:** Dev Charaya · **Role:** Data Engineer Intern @ Celebal Technologies

</div>

---

## 📌 Project Overview

This repository contains the Week-05 assignment for the **Celebal Technologies Data Engineering Internship**, focused on building practical skills with **Apache Spark DataFrames**. The project walks through Spark fundamentals, the limitations of MapReduce, and a complete hands-on data pipeline — covering everything from raw data ingestion to a cleaned, aggregated, and schema-validated final output.

A custom synthetic dataset was created specifically to exercise every concept required by the assignment, since no official dataset was provided.

---

## 🎯 Objectives

This project is designed to build a solid understanding of:

- ⚙️ Spark fundamentals and architecture
- 🐢 Limitations of traditional MapReduce
- 🚀 In-memory computing and why it makes Spark faster
- 🧱 Spark DataFrame concepts
- 🔒 DataFrame immutability
- 🧹 Data cleaning techniques
- 🔄 Data transformation
- 🔍 Filtering operations
- 📊 Aggregation and grouping operations
- 🔀 Shuffle operations
- 🧬 Schema modifications
- 🏗️ Building an end-to-end Spark data processing pipeline

---

## 🛠️ Technology Stack

| Category | Tools |
|---|---|
| **Language** | Python 3.12 |
| **Processing Engine** | Apache Spark (PySpark) |
| **Runtime** | Java 17 (Temurin JDK) |
| **Development** | Jupyter Notebook, VS Code |
| **Data Handling** | Pandas |
| **Version Control** | Git & GitHub |

---

## ☕ Java Configuration (Important)

While setting up the environment, a Java compatibility issue was encountered and resolved.

> **❌ Problem:** Java 23 caused PySpark runtime issues.
>
> **Error:**
> ```
> UnsupportedOperationException: getSubject is supported only if a security manager is allowed
> ```
>
> **✅ Solution:** Installed Java 17 LTS and configured the environment variable.

**`JAVA_HOME`**
```
C:\Program Files\Eclipse Adoptium\jdk-17.0.19.10-hotspot
```

**Verification command:**
```bash
java --version
```

**Result:**
```
openjdk 17.0.19
```

> 💡 **Takeaway:** PySpark works best with Java LTS versions (8, 11, or 17). Always verify Java compatibility before setting up a Spark environment.

---

## 🗂️ Dataset Information

| Detail | Description |
|---|---|
| **File** | `spark_synthetic_dataset.csv` |
| **Origin** | Custom-created, as no official dataset was provided for this assignment |
| **Purpose** | Designed to satisfy all Week-05 assignment requirements |

**Columns:**

`user_id` · `transaction_date` · `region` · `product_category` · `sale_amount` · `city` · `age` · `subscription` · `price` · `store_id` · `email` · `username` · `raw_timestamp`

---

## 📝 Assignment Questions Covered

| # | Topic |
|---|---|
| Q1 | MapReduce limitations |
| Q2 | In-memory computing |
| Q3 | Remove duplicates |
| Q4 | Filter and aggregate sales data |
| Q5 | Handle null values |
| Q6 | Count records by city |
| Q7 | DataFrame immutability |
| Q8 | Age and subscription filtering |
| Q9 | Importance of handling null values before aggregation |
| Q10 | Schema modification and timestamp conversion |
| Q11 | Shuffle operations |
| Q12 | Remove invalid records |
| Q13 | Multiple aggregations using `.agg()` |
| Q14 | Risks of `inferSchema` |
| Q15 | End-to-end processing pipeline |

---

## 🔁 Processing Pipeline

The notebook follows a structured, step-by-step workflow:

```
1.  Create Spark Session
2.  Load dataset
3.  Explore dataset
4.  Check schema
5.  Check missing values
6.  Remove duplicates
7.  Handle null values
8.  Apply filtering conditions
9.  Perform aggregations
10. Group data
11. Modify schema
12. Build final processing pipeline
13. Save processed outputs
```

---

## 📤 Output Files

| File | Description |
|---|---|
| `cleaned_dataset.csv` | Dataset after duplicate removal and null handling |

---

## 📁 Folder Structure

```
Week-05-Spark-DataFrame-Processing/
│
├── data/
│   └── spark_synthetic_dataset.csv
│
├── notebook/
│   └── week5_spark_assignment.ipynb
│
├── output/
│  └── cleaned_dataset.csv
│   
│
├── README.md
└── .gitignore
```

---

## 💡 Key Learnings

- ⚡ Spark is faster than MapReduce because of **in-memory processing**.
- 🔒 Spark DataFrames are **immutable** — transformations return new DataFrames.
- 🧹 Data cleaning should always be performed **before** aggregations.
- 🔀 `groupBy()` operations trigger a **shuffle** across partitions.
- 🧬 Proper schema management significantly improves data quality.
- 🏗️ Building an **end-to-end pipeline** is essential for scalable data engineering.

---

## 🚀 Future Improvements

- [ ] Integrate with a distributed storage system (e.g., HDFS or S3)
- [ ] Add automated unit tests for transformation logic
- [ ] Convert notebook pipeline into modular, reusable PySpark scripts
- [ ] Add performance benchmarking (in-memory vs. disk-based comparisons)
- [ ] Introduce Spark SQL-based querying as an alternative pipeline
- [ ] Add CI/CD for automated pipeline validation

---

<div align="center">

### 👤 Author

**Dev Charaya**
Data Engineer Intern · Celebal Technologies

📂 *Part of the Celebal Technologies Data Engineering Internship Program*

</div>