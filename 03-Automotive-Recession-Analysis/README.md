# Automotive Sales & Recession Impact Analysis 🚗📉

**Author:** Zaara Shaikh
**Tech Stack:** Python, Dash, Plotly, Matplotlib, Seaborn, Folium

## 📖 Project Overview
This project analyzes the impact of historical economic recessions on the automotive industry. As a Data Analyst for *XYZAutomotives*, the goal was to identify consumer purchasing behaviors during crisis periods to inform future marketing and inventory strategies.

The project is divided into two distinct components:
1.  **Exploratory Data Analysis (EDA):** A static analysis using Matplotlib and Seaborn to visualize trends in GDP, unemployment, and vehicle sales.
2.  **Interactive Dashboard:** A web-based application utilizing **Dash and Plotly** to allow users to dynamically filter data by year and recession status.

## 📊 Key Insights
* **Recession Impact:** Sales of sports and luxury vehicles decline significantly during recessions, while medium-family cars remain relatively stable.
* **Seasonality:** Sales volume shows distinct seasonal patterns, often dipping in winter months and peaking in mid-year.
* **Advertising Efficacy:** Marketing expenditure yields diminishing returns during recession periods compared to non-recession years.

## 🚀 How to Run the Dashboard
To interact with the dashboard locally:

1.  Clone this repository.
2.  Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the application:
    ```bash
    python Automotive_Sales_Dashboard.py
    ```
4.  Open your browser and navigate to `http://127.0.0.1:8050/`.

## 📂 Repository Structure
* `Automotive_Sales_Recession_Analysis.ipynb`: Detailed EDA and static visualizations.
* `Automotive_Sales_Dashboard.py`: Source code for the interactive Dash web application.

## 🤝 Project Context & Acknowledgements
This project was completed as part of the **IBM Data Science Professional Certificate**.
* **Scenario & Dataset:** Provided by IBM/Coursera.
* **Implementation:** I was responsible for developing the visualization logic, implementing the Dash callbacks, and refining the data processing pipeline within the provided framework.
