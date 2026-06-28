<div align="center">

# ⚡ Week-06 · Apache Spark Data Processing & Optimization

### Celebal Technologies — Data Engineer Internship · Week 06 Assignment

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Apache Spark](https://img.shields.io/badge/Apache%20Spark-3.x-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)](https://spark.apache.org/)
[![PySpark](https://img.shields.io/badge/PySpark-DataFrame%20API-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)](https://spark.apache.org/docs/latest/api/python/)
[![Java](https://img.shields.io/badge/Java-17-007396?style=for-the-badge&logo=openjdk&logoColor=white)](https://openjdk.org/projects/jdk/17/)
[![Hadoop](https://img.shields.io/badge/Hadoop-Winutils-66CCFF?style=for-the-badge&logo=apachehadoop&logoColor=black)](https://hadoop.apache.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Parquet](https://img.shields.io/badge/Apache-Parquet-50ABF1?style=for-the-badge&logo=apache&logoColor=white)](https://parquet.apache.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)
[![Status](https://img.shields.io/badge/Status-Completed-28a745?style=for-the-badge)](.)

---

*A fully completed, industry-grade Apache Spark assignment covering DataFrame operations, performance optimization, lazy evaluation, DAG analysis, and columnar storage — built during a professional Data Engineering internship.*

</div>

---

## 📋 Table of Contents

- [📌 Project Overview](#-project-overview)
- [🗂️ Repository Structure](#️-repository-structure)
- [✨ Features](#-features)
- [📊 Dataset](#-dataset)
- [📓 Assignment Questions](#-assignment-questions)
- [🚧 Challenges Faced](#-challenges-faced)
- [🎓 Learning Outcomes](#-learning-outcomes)
- [🛠️ Technologies Used](#️-technologies-used)
- [⚙️ Installation & Setup](#️-installation--setup)
- [▶️ Running the Project](#️-running-the-project)
- [📈 Results](#-results)
- [🚀 Future Improvements](#-future-improvements)

---

## 📌 Project Overview

This project is the **Week 06 assignment** of the **Celebal Technologies Data Engineer Internship**. It demonstrates a comprehensive, hands-on understanding of **Apache Spark** — one of the most widely used distributed data processing frameworks in modern data engineering.

> **Objective:** Understand Apache Spark architecture and perform efficient large-scale data processing using Spark DataFrames, Transformations, Actions, Filtering, Schema Handling, CSV/Parquet I/O, and Performance Optimization techniques including Lazy Evaluation, DAG analysis, and Predicate Pushdown.

The notebook answers all **15 assignment questions** in full, with:

- ✅ Clear question titles
- ✅ Conceptual explanations
- ✅ PySpark implementation
- ✅ Verified output
- ✅ Conclusions for each question

---

## 🗂️ Repository Structure

```
Week-06-Apache-Spark-Data-Processing/
│
├── 📁 Data/
│   ├── 📄 source.csv                        # Custom dataset (CSV format)
│   └── 📁 parquet_output/
│       └── 📄 source.parquet                # Parquet-converted dataset
│
├── 📁 csv_output/
│   ├── 📄 part-00000-*.csv                  # Spark-generated CSV output
│   ├── 📄 _SUCCESS                          # Spark job success marker
│   └── 📄 _SUCCESS.crc                      # CRC checksum file
│
├── 📁 notebook/
│   └── 📓 Spark_Data_Processing_and_Optimization.ipynb
│
├── 📄 README.md                             # Project documentation (this file)
└── 📄 .gitignore                            # Git ignore configuration
```

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔥 **Spark DataFrame API** | Full DataFrame operations — read, write, filter, transform |
| 📂 **CSV Processing** | Schema inference, reading and writing CSV via PySpark |
| 🗃️ **Parquet Processing** | Efficient columnar storage with Parquet read/write |
| ⏳ **Lazy Evaluation** | Understanding how Spark defers computation until an action is triggered |
| 🔗 **DAG Analysis** | Directed Acyclic Graph lineage tracking for Spark jobs |
| 🔍 **Schema Inference** | Automatic schema detection from structured datasets |
| 🔄 **Column Transformations** | Renaming, casting, and computing new columns |
| 🎯 **Filtering** | Single and multi-condition row filtering |
| 🛠️ **Data Type Casting** | Converting columns to appropriate types |
| ❌ **Null Handling** | Managing missing and null values in DataFrames |
| ⚡ **Predicate Pushdown** | Query optimization by pushing filters closer to the data source |
| 🏗️ **Spark Architecture** | Driver, Executors, Cluster Manager concepts |
| 🖥️ **Deployment Modes** | Client Mode vs Cluster Mode comparison |
| 📊 **Transformations vs Actions** | Clear differentiation between lazy and eager operations |

---

## 📊 Dataset

> **Note:** The assignment did not provide a dataset. A **custom dataset was professionally designed and created** specifically for this assignment to best demonstrate all required Apache Spark concepts.

The dataset is structured to showcase:

- DataFrame creation and schema inference
- CSV reading and writing
- Parquet conversion and reading
- Column operations and transformations
- Filtering with single and multiple conditions
- Data type casting
- Null value handling

The dataset is located at: `Data/source.csv`

---

## 📓 Assignment Questions

The notebook contains complete solutions to all **15 assignment questions**:

| # | Question Topic | Concepts Covered |
|---|---|---|
| Q1 | **Spark Architecture** | Driver, Executors, Cluster Manager |
| Q2 | **Lazy Evaluation** | Transformations deferred until action |
| Q3 | **Reading CSV** | Schema inference, SparkSession, DataFrame |
| Q4 | **CSV vs Parquet** | Format comparison, storage efficiency |
| Q5 | **Filtering & Selection** | `.filter()`, `.select()`, column expressions |
| Q6 | **Rename Columns & Cast Data Types** | `.withColumnRenamed()`, `.cast()` |
| Q7 | **Lineage Graph** | DAG, job stages, RDD lineage |
| Q8 | **Multiple Conditions** | AND logic in filter expressions |
| Q9 | **Predicate Pushdown** | Query optimization, Parquet filter pushdown |
| Q10 | **Add New Column** | `.withColumn()`, derived column computation |
| Q11 | **Transformations vs Actions** | Lazy vs eager execution model |
| Q12 | **Read Parquet → Filter → Save CSV** | End-to-end Parquet pipeline |
| Q13 | **Client Mode vs Cluster Mode** | Deployment architecture comparison |
| Q14 | **OR Filtering** | OR logic, `.filter()` with multiple conditions |
| Q15 | **show() vs collect()** | Driver memory, performance implications |

> 📓 All solutions, explanations, code, outputs, and conclusions are inside the notebook:
> `notebook/Spark_Data_Processing_and_Optimization.ipynb`

---

## 🚧 Challenges Faced

### ⚙️ Hadoop Native Binaries on Windows (Q12)

During implementation of **Question 12** — reading a Parquet file, applying filters, and saving the result as CSV — Apache Spark on **Windows** required **Hadoop native binaries** to complete Parquet I/O operations.

This is a standard and well-known requirement for running Apache Spark on Windows environments, and resolving it was a valuable hands-on learning experience in Spark environment configuration.

**Steps completed to resolve this:**

```
✅ Downloaded and installed Hadoop Winutils for the correct Hadoop version
✅ Configured the HADOOP_HOME environment variable
✅ Added %HADOOP_HOME%\bin to the Windows System PATH
✅ Verified Java 17 compatibility with the installed PySpark version
✅ Restarted the Spark environment and Jupyter kernel
✅ Successfully generated Parquet output
✅ Successfully loaded and read Parquet files using Spark
✅ Successfully exported the filtered result as CSV
```

> 💡 **Key Takeaway:** Hadoop native library configuration is a **common and expected requirement** for Apache Spark development on Windows. Understanding environment setup is a core skill for any Data Engineer working with distributed systems.

---

## 🎓 Learning Outcomes

### 🏗️ Apache Spark Architecture
- Understood the roles of **Driver**, **Executors**, and **Cluster Manager**
- Explored **Client Mode** vs **Cluster Mode** deployment strategies
- Analyzed how Spark distributes and parallelizes computation

### ⏳ Execution Model
- Mastered **Lazy Evaluation** — transformations are not executed until an action is called
- Explored **Directed Acyclic Graph (DAG)** and how Spark optimizes job execution
- Differentiated between **Transformations** (lazy) and **Actions** (eager)

### 📂 Data Formats & I/O
- Read and wrote **CSV** files with automatic schema inference
- Converted data to **Parquet** for columnar, compressed storage
- Applied end-to-end pipelines: Parquet → Filter → CSV

### 🔄 DataFrame Operations
- Applied **filtering**, **selection**, and **column transformations**
- Renamed columns using `.withColumnRenamed()`
- Added derived columns using `.withColumn()`
- Cast data types using `.cast()`

### ⚡ Performance Optimization
- Applied **Predicate Pushdown** to optimize Parquet reads
- Understood how pushing filters to the storage layer reduces I/O

### 🪟 Windows Environment Configuration
- Installed and configured **Hadoop Winutils**
- Set `HADOOP_HOME` and updated Windows `PATH`
- Configured **Java 17** for compatibility with PySpark
- Learned Spark environment troubleshooting on Windows

---

## 🛠️ Technologies Used

<div align="center">

| Technology | Version | Purpose |
|---|---|---|
| ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) | 3.10+ | Core programming language |
| ![Apache Spark](https://img.shields.io/badge/-Apache%20Spark-E25A1C?logo=apachespark&logoColor=white) | 3.x | Distributed data processing engine |
| ![PySpark](https://img.shields.io/badge/-PySpark-E25A1C?logo=apachespark&logoColor=white) | 3.x | Python API for Apache Spark |
| ![Parquet](https://img.shields.io/badge/-Apache%20Parquet-50ABF1?logo=apache&logoColor=white) | — | Columnar storage format |
| ![Jupyter](https://img.shields.io/badge/-Jupyter-F37626?logo=jupyter&logoColor=white) | — | Interactive notebook environment |
| ![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white) | 1.x+ | Data manipulation and analysis |
| ![Java](https://img.shields.io/badge/-Java%2017-007396?logo=openjdk&logoColor=white) | 17 | JVM runtime for Spark |
| ![Hadoop](https://img.shields.io/badge/-Hadoop%20Winutils-66CCFF?logo=apachehadoop&logoColor=black) | — | Native binaries for Windows |
| ![Git](https://img.shields.io/badge/-Git-F05032?logo=git&logoColor=white) | — | Version control |
| ![GitHub](https://img.shields.io/badge/-GitHub-181717?logo=github&logoColor=white) | — | Repository hosting |

</div>

---

## ⚙️ Installation & Setup

### Prerequisites

Ensure the following are installed before running the project:

- **Python** 3.10 or higher
- **Java 17** (required by Apache Spark)
- **Hadoop Winutils** *(Windows only)*

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/Week-06-Apache-Spark-Data-Processing.git
cd Week-06-Apache-Spark-Data-Processing
```

### 2️⃣ Install Python Dependencies

```bash
pip install pyspark pandas pyarrow jupyter
```

### 3️⃣ Configure Java 17

Ensure `JAVA_HOME` points to your Java 17 installation:

```bash
# Windows (PowerShell)
$env:JAVA_HOME = "C:\Program Files\Java\jdk-17"

# Linux / macOS
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk
```

### 4️⃣ Configure Hadoop Winutils *(Windows Only)*

```bash
# 1. Download Hadoop Winutils (matching your Hadoop version)
# 2. Place winutils.exe in: C:\hadoop\bin\

# Set environment variables (PowerShell or System Properties)
$env:HADOOP_HOME = "C:\hadoop"
$env:PATH += ";C:\hadoop\bin"
```

> 💡 Hadoop Winutils is required on Windows for Spark to perform file system operations, including Parquet read/write.

---

## ▶️ Running the Project

```bash
# Step 1 — Launch Jupyter Notebook
jupyter notebook

# Step 2 — Open the assignment notebook
# Navigate to: notebook/Spark_Data_Processing_and_Optimization.ipynb

# Step 3 — Run all cells in order
# Use: Kernel → Restart & Run All

# Step 4 — Observe outputs
# ✅ DataFrame outputs printed in notebook cells
# ✅ CSV output written to: csv_output/
# ✅ Parquet output written to: Data/parquet_output/
```

---

## 📈 Results

Upon successful execution of the notebook:

| Result | Description |
|---|---|
| ✅ Dataset Loaded | Custom CSV dataset loaded into a Spark DataFrame |
| ✅ Schema Inferred | Column names and data types automatically detected |
| ✅ Transformations Applied | Columns renamed, cast, and new columns derived |
| ✅ Filtering Completed | Single and multi-condition filtering demonstrated |
| ✅ Parquet Generated | Dataset written to columnar Parquet format |
| ✅ CSV Generated | Filtered Parquet data exported back to CSV |
| ✅ Performance Concepts Demonstrated | Lazy evaluation, DAG, and Predicate Pushdown explained and applied |
| ✅ All 15 Questions Answered | Complete solutions with outputs and conclusions |

---

## 🚀 Future Improvements

The following enhancements could extend this project further:

| Improvement | Description |
|---|---|
| 🔷 **Spark SQL** | Query DataFrames using SQL syntax via `spark.sql()` |
| 🌊 **Spark Streaming** | Real-time data processing with Structured Streaming |
| 🤖 **MLlib** | Machine learning pipelines built on Spark DataFrames |
| ☁️ **Azure Databricks** | Cloud-native Spark execution with notebook collaboration |
| 🔁 **Azure Data Factory** | Orchestrated data pipelines using ADF + Spark |
| 🔺 **Delta Lake** | ACID-compliant, versioned data lake storage on Spark |
| 📨 **Apache Kafka** | Streaming ingestion pipeline: Kafka → Spark → Parquet |
| 🌐 **Cloud Deployment** | Deploy Spark jobs on AWS EMR, Azure HDInsight, or GCP Dataproc |

---

<div align="center">

---

### 🌟 If this project was helpful, consider giving it a star!

**Celebal Technologies · Data Engineer Internship · Week 06**

*Built with 💙 using Apache Spark, PySpark, and Python*

---

</div>
