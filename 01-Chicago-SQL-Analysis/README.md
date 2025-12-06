# Chicago City Socioeconomic & Crime Analysis 🏙️🔍

**Tools:** SQL (SQLite), Python, Pandas

## 📖 Project Overview
This project examines the correlation between socioeconomic hardship and criminal activity in Chicago using three real-world datasets:
1.  **Census Data:** Socioeconomic indicators by community area.
2.  **Crime Data:** Reported incidents from 2001 to present.
3.  **School Data:** Performance and safety scores of public schools.

## 📊 Key Findings
* **Hardship Correlation:** Areas with a "Hardship Index" > 50 (e.g., Riverdale) consistently show higher crime rates.
* **Safety in Schools:** "Criminal Trespass" and "Battery" are the most common crimes reported on school grounds.
* **Data Integrity:** Executed advanced SQL JOINs to bridge disparate datasets, revealing that crime is concentrated in specific police districts rather than being evenly distributed.

## ⚙️ How to View
* Open the `.ipynb` file to see the SQL queries and result sets.
* The database connection is handled via `sqlite3` within the notebook.
