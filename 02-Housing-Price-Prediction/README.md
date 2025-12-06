# Seattle Housing Price Prediction Model 🏠📈

**Tools:** Scikit-Learn, Pandas, NumPy, Seaborn

## 📖 Project Overview
A predictive modeling project for a hypothetical Real Estate Investment Trust (REIT). The goal was to determine the market price of houses in King County, USA (Seattle area) based on features like square footage, waterfront views, and condition.

## 🧠 Model Evolution & Accuracy ($R^2$)
I tested multiple regression approaches to find the best fit:
1.  **Simple Linear Regression:** $R^2 \approx 0.49$ (Poor fit).
2.  **Multiple Linear Regression:** $R^2 \approx 0.65$ (Better, but high variance).
3.  **Polynomial Ridge Regression (The Winner):** $R^2 \approx 0.75$.

## 🚀 Key Achievements
* **Feature Engineering:** Identified that `sqft_living` and `grade` are the strongest price indicators.
* **Pipeline Construction:** Built a scikit-learn Pipeline to automate Scaling $\rightarrow$ Polynomial Transformation $\rightarrow$ Ridge Regression.
* **Outlier Analysis:** Visualized the massive price variance in "Waterfront" properties using Boxplots.
