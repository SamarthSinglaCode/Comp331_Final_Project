# Comp331_Final_Project
Nutrition Data Quality Analysis
This repository contains the work completed for my COMP 331 – Data Quality project. The objective of this project is to evaluate the quality of real-world nutritional datasets and understand how data quality issues impact analytics, data warehousing processes, and machine learning applications—particularly in the context of personalized nutrition and health-risk assessment systems.

📘 Project Description
Modern nutrition datasets are widely used in health applications, mobile food scanners, calorie-tracking apps, and machine learning models that evaluate whether a food item is healthy or risky for certain health conditions. However, these datasets often suffer from poor quality due to inconsistent reporting, crowdsourced data entry, and heterogeneous data sources.

This project focuses on conducting a detailed data quality assessment of two major publicly available food datasets:

USDA FoodData Central

Open Food Facts

Both datasets contain information such as product names, brands, barcodes, nutritional values (calories, sugar, fat, sodium), ingredients, serving sizes, and categories. These datasets are commonly used to build systems that analyze nutritional health, predict risks for users with conditions like diabetes or hypertension, and provide personalized dietary recommendations.

🎯 Project Goals
The primary goal of this project is to apply data quality concepts from Weeks 10–11 (Data Warehousing and Data Mining) to identify and evaluate real data quality problems. Specifically, the project aims to:

1. Assess Key Data Quality Dimensions
Completeness – Identify missing nutrient fields, incomplete product labels, and gaps in essential data.

Consistency – Detect unit mismatches, inconsistent naming conventions, and repeated or conflicting categories.

Validity – Identify impossible nutrient values, incorrect barcode formats, and contradictory entries.

2. Connect Theory to Real Data
Using concepts from the course:

Data warehouse ETL workflows

Conformed dimensions

Fact table loading rules

Preprocessing for machine learning

Handling missing values, outliers, and noise

the analysis shows how poor data quality affects downstream tasks.

3. Support Personalized Nutrition Models
Since the broader project idea involves building a machine learning system that:

classifies food as healthy/moderate/unhealthy

predicts sugar, fat, or sodium levels

gives personalized warnings for health conditions

high-quality data becomes essential.
This analysis helps ensure the foundation for such systems is reliable.

Key Insights
During the data quality assessment, several important findings emerged:

Completeness Issues
Missing sugar, sodium, vitamin, and serving size fields

Partial nutrition profiles across different product categories

Incomplete labels from user-submitted entries

Consistency Issues
Energy recorded as both kcal and kJ

Sodium stored as mg in some records and g in others

Brands like “Coca-Cola,” “Coca Cola,” and “coca cola” treated as different entities

Category duplication and inconsistent formatting

Validity Issues
Sugar_100g values > 100 g

Negative values for fat or energy

Incorrect barcode formats (non-numeric or wrong digit length)

Products marked “sugar-free” but containing measurable sugar

These issues create major challenges for data warehousing (ETL staging, dimension cleaning) and machine learning (feature scaling, outlier removal, training stability).

🛠 Tools and Techniques Used
Python (Pandas, NumPy) for data profiling and cleaning

Jupyter Notebook for exploratory analysis

Data Warehousing Concepts

ETL pipelines

Conformed dimensions

Fact vs. dimension table issues

Data Mining Concepts

Handling missing data

Outlier detection

Normalization and standardization

Noise reduction
