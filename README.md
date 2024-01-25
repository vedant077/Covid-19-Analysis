# Covid-19 Data Analysis

## Overview
This project focuses on transforming raw data using SQL, storing the processed data in a postgres database, and creating a descriptive Power BI dashboard for state and county-level analysis. Additionally, a Python script has been developed to provide monthly/weekly notifications to stakeholders about the top 10 states or counties with the highest number of deaths. Moreover, an alert system has been implemented to notify stakeholders when a particular county exceeds an expected threshold, triggering a detailed email about the number of deaths in that specific county.

## Project Components

### 1. Data Transformation (SQL)
Raw data undergoes comprehensive transformations using SQL queries to prepare it for analysis. This step involves cleaning, filtering, and structuring the data to ensure accuracy and relevance.

### 2. Database Storage
The transformed data is stored in an open-source postgres database for efficient retrieval and management. This step ensures that the processed data is readily available for analysis and reporting.

### 3. Power BI Dashboard
A descriptive Power BI dashboard has been developed to provide insightful visualizations for both state and county-level analysis. The dashboard includes key metrics, trends, and interactive visualizations to facilitate a comprehensive understanding of the data.

![Screenshot 2024-01-25 015012](https://github.com/vedant077/Covid-19-Analysis/assets/58139698/c87e406e-ca2b-4b08-941d-38494c325a78)

![Screenshot 2024-01-25 014837](https://github.com/vedant077/Covid-19-Analysis/assets/58139698/f38e5d51-fe1b-49f9-a708-d883768f78c5)

### 4. Notification System (Python Script)
A Python script has been implemented to provide weekly notifications to stakeholders about the top 10 states or counties with the highest number of deaths. Additionally, an alert system triggers an email when a specific county surpasses the expected threshold, ensuring stakeholders are promptly informed about critical developments.

![email_alert](https://github.com/vedant077/Covid-19-Analysis/assets/58139698/7d6f1f0b-d1cf-44f6-b995-4a1af518d558)

## Dependencies
- Postgres DB 
- Power BI Desktop
- Python (with required libraries specified in the Python script)

