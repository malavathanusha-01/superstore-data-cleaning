# superstore-data-cleaning
End-to-end data cleaning and preprocessing project using the Superstore dataset. Includes data profiling, handling missing values, removing duplicates, feature engineering, and generating an analysis-ready dataset using Python (Pandas).
# 📊 Superstore Data Cleaning & Preprocessing

## 🔹 Overview
This project focuses on **end-to-end data cleaning and preprocessing** of the Superstore dataset. The objective is to transform raw data into a **clean, structured, and analysis-ready format**, which is a critical first step in any data analytics workflow.

---

## 🎯 Project Objectives
- Understand dataset structure and business context  
- Identify and fix data quality issues  
- Perform data transformation and feature engineering  
- Prepare dataset for analysis and visualization  

---

## 📁 Dataset
- **Name:** Sample Superstore Dataset  
- **Type:** Sales/Transactional Data  
- **Contains:**
  - Orders, Customers, Products  
  - Sales, Profit, Discount  
  - Shipping and Regional details  

---

## ⚙️ Tasks Performed

### ✅ 1. Data Loading
- Imported dataset using Pandas  
- Handled encoding issues (`latin1`)  

### ✅ 2. Data Profiling
- Checked dataset structure (`info()`, `head()`)  
- Identified:
  - Missing values  
  - Duplicate records  
  - Incorrect data types  
  - Outliers  

### ✅ 3. Data Cleaning
- Filled missing values (e.g., Postal Code)  
- Removed duplicate rows  
- Standardized text fields  
- Converted date columns to datetime format  

### ✅ 4. Feature Engineering
Created new columns:
- **Delivery Days** → Shipping delay  
- **Profit Margin** → Profitability ratio  

### ✅ 5. Outlier Handling
- Removed extreme values using 99th percentile filtering  

### ✅ 6. Final Output
- Exported cleaned dataset: `cleaned_superstore.csv`  

---

## 🛠️ Tools & Technologies
- Python  
- Pandas  
- VS Code / Jupyter Notebook  

---

## 📂 Repository Structure
