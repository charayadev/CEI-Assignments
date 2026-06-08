# 📊 Week 3 – Advanced SQL Analytics Using Subqueries, CTEs, and Window Functions

<div align="center">

![SQL](https://img.shields.io/badge/SQL-Advanced-blue?style=for-the-badge&logo=postgresql&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![pgAdmin](https://img.shields.io/badge/pgAdmin-4-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![Internship](https://img.shields.io/badge/CEI-Week%203-orange?style=for-the-badge)

**Celebal Excellence Internship (CEI) · MCA Data Science · JECRC University**

</div>

---

## 📌 Project Overview

This repository contains the Week 3 assignment for the **Celebal Excellence Internship (CEI)** program. The objective was to move beyond basic SQL and apply advanced analytical techniques — **Subqueries**, **Common Table Expressions (CTEs)**, and **Window Functions** — to derive meaningful business insights from a real-world retail dataset.

All queries were written and executed in **PostgreSQL** using **pgAdmin 4**, demonstrating practical skills that are directly applicable in data analytics and data engineering roles.

---

## 🎯 Objective

- Master advanced SQL constructs: Subqueries, CTEs, and Window Functions
- Normalize a flat CSV dataset into structured relational tables
- Perform customer-level sales analysis using layered SQL logic
- Produce ranked and segmented insights from transactional data
- Build a mini analytics project from raw data import to final reporting

---

## 🗂️ Dataset Overview

| Property | Details |
|---|---|
| **Dataset** | Superstore Dataset |
| **Source** | [Kaggle – Superstore Dataset Final](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) |
| **Format** | CSV |
| **Domain** | US Retail / E-Commerce Sales |
| **Database** | PostgreSQL |
| **Tool** | pgAdmin 4 |

The Superstore dataset is a widely-used retail dataset containing order-level transactional records including customer details, product categories, sales figures, discounts, and profit data.

---

## 🛠️ Database Setup Process

1. **Downloaded** the Superstore dataset CSV from Kaggle
2. **Created** a raw staging table `superstore_raw` in PostgreSQL
3. **Imported** all CSV records into `superstore_raw` using pgAdmin 4's import utility
4. **Explored** the dataset structure and validated successful import
5. **Normalized** the raw table into three clean, relational tables using `SELECT DISTINCT`

---

## 🗄️ Tables Created

| Table | Description |
|---|---|
| `superstore_raw` | Raw staging table containing all imported CSV data |
| `customers` | Normalized customer dimension table (distinct customers) |
| `orders` | Normalized orders fact table |
| `products` | Normalized product dimension table |

---

## 🧠 SQL Concepts Covered

| Category | Concepts |
|---|---|
| **Subqueries** | Scalar subqueries, correlated subqueries, subqueries in `WHERE` and `FROM` |
| **CTEs** | `WITH` clause, multi-step CTE chains, readable query decomposition |
| **Window Functions** | `RANK()`, `DENSE_RANK()`, `ROW_NUMBER()`, `PARTITION BY`, `ORDER BY` within frame |
| **Joins** | `INNER JOIN` across normalized tables |
| **Aggregations** | `SUM()`, `AVG()`, `COUNT()` with `GROUP BY` |
| **Filtering & Sorting** | `WHERE`, `HAVING`, `ORDER BY`, `LIMIT` |

---

## 📋 Query Summary

| # | Query Description | Concepts Used |
|---|---|---|
| 1 | Find all orders where sales > average sales | Subquery, `AVG()` |
| 2 | Find the highest sales order for each customer | Correlated subquery, `MAX()` |
| 3 | Calculate total sales per customer | CTE, `SUM()`, `GROUP BY` |
| 4 | Find customers whose total sales are above average | CTE, `AVG()`, `HAVING` |
| 5 | Rank all customers based on total sales | CTE, `RANK()`, Window Function |
| 6 | Assign row numbers to each order within a customer | `ROW_NUMBER()`, `PARTITION BY` |
| 7 | Display top 3 customers by total sales | CTE, `RANK()`, `WHERE rank <= 3` |
| 8 | Final combined query: Customer Name, Total Sales, Rank | `JOIN` + CTE + Window Function |

---

## 🏗️ Mini Project — Customer Sales Insights

A focused analytics project using the Superstore dataset to generate actionable customer-level insights:

| Analysis | Description |
|---|---|
| **Top 5 Customers** | Highest revenue-generating customers by total sales |
| **Bottom 5 Customers** | Lowest revenue-generating customers by total sales |
| **Single-Order Customers** | Customers who placed only one order |
| **Above-Average Sales Customers** | Customers whose total sales exceed the dataset average |
| **Highest Order Value per Customer** | Maximum single-order sales amount for each customer |

---

## 📈 Key Findings

### 🏆 Top 5 Customers by Total Sales

| Rank | Customer Name | Total Sales ($) |
|---|---|---|
| 1 | Sean Miller | 25,043.07 |
| 2 | Tamara Chand | 19,052.22 |
| 3 | Raymond Buch | 15,117.35 |
| 4 | Tom Ashbrook | 14,595.62 |
| 5 | Adrian Barton | 14,473.57 |

### 📉 Bottom 5 Customers by Total Sales

| Rank | Customer Name | Total Sales ($) |
|---|---|---|
| 1 | Thais Sissman | 4.84 |
| 2 | Lela Donovan | 5.30 |
| 3 | Carl Jackson | 16.52 |
| 4 | Mitch Gastineau | 16.74 |
| 5 | Roy Skaria | 22.33 |

### 📊 Summary Statistic

| Metric | Value |
|---|---|
| Customers with Above-Average Total Sales | **294** |

---

## 💡 Learning Outcomes

- Writing **multi-step CTEs** to break complex queries into readable, maintainable logic
- Applying **window functions** (`RANK`, `DENSE_RANK`, `ROW_NUMBER`) for within-group analytics
- Using **correlated subqueries** to perform row-level comparisons against aggregate values
- **Normalizing flat data** into a proper relational schema using `SELECT DISTINCT`
- Combining `JOIN`, CTE, and Window Functions in a single production-quality query
- Interpreting query results to derive **business insights** from raw transactional data

---

## 📁 Repository Structure

```
Week-03-SQL-Advanced-Analytics/
│
├── Week_3.sql        # All SQL queries: setup, analysis, and mini project
└── README.md         # Project documentation (this file)
```

---

## ⚙️ Technologies Used

| Technology | Purpose |
|---|---|
| **PostgreSQL** | Relational database engine |
| **pgAdmin 4** | GUI for writing and executing SQL queries |
| **SQL** | Data import, normalization, and analysis |
| **Kaggle** | Dataset source |

---

## 👤 Author

<div align="center">

**Dev Charaya**
MCA Data Science · JECRC University
Celebal Excellence Internship (CEI) · Week 3

</div>

---

<div align="center">

*Part of the Celebal Excellence Internship (CEI) – MCA Data Science Track*

</div>
