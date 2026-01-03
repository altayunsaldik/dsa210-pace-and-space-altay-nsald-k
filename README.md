DSA 210 Project Proposal: The "Pace and Space" Revolution: Analysis of Three-Point Shooting and Game Tempo in the NBA

Course: DSA 210 Introduction to Data Science
Term: 2025-2026 Fall Term
Student:Altay Ünsaldık 34079


---

1. Project Proposal

1.1. Motivation and Objectives

The modern NBA has undergone a significant strategic transformation, widely characterized as the "Pace and Space" era. This evolution is defined by an increased statics on offensive spacing ("Space") and huge rise in the volume of three-point shot attempts (3PA).

While the "Pace and Space" term is widely used, the statistical relationship between these two terms are not always noticed. "Pace" refers to the game's tempo, formally measured as the number of possessions a team uses per 48 minutes. This project aims to search the statistical relationship between the strategic shift towards three-point shooting and the resulting change in game tempo.

The primary objective is to quantify this relationship, moving beyond observation to provide a data-driven analysis of how the NBA's offensive philosophy has evolved.

1.2. Research Questions

This study will address these following core research questions:

1.  What is the longitudinal trend of league-average `Pace` and `3PA` from the 2000 to 2025 season?
2.  Is there a statistically significant relationship between a team's number of three-point attempts (`3PA`) and its `Pace`?
3.  To what extent can a team's `Pace` be explained by its shot selection? We will develop a multivariate linear regression model to quantify the impact of `3PA`, `2PA` (two-point attempts), and `FTA` (free-throw attempts) on the `Pace` variable.
4.  How does offensive efficiency mediate the relationship between Pace and team winning percentage?


2. Data and Acquisition Methodology

2.1. Data Source and Structure

The data is sourced from Basketball-Reference.com, a validated public domain for NBA statistics. The core of this analysis relies on constructing a balanced panel dataset spanning 25 seasons (2000-01 to 2024-25) and covering approximately 750 team-seasons (≈30 teams×25 seasons).

2.2. Panel Data Construction and Feature Engineering

This project employs a two-stage data acquisition and feature engineering strategy to construct the final analytical dataset.

Base Datasets (Raw Acquisition):

Team Per Game Stats: Essential for volume metrics: 3PA, 2PA, FTA.

Team Advanced Statistics: Essential for dependent and control variables: Pace, Winning Percentage.

Team Shooting Stats: Essential for efficiency metrics: 3P%, eFG%. (This formalizes the use of the "Couple More Datasets" into the core plan).

Data Enrichment and Feature Engineering:

Panel Key: Datasets will be rigorously merged using the composite key (Team and Year) to establish the panel structure necessary for fixed-effects modeling.

Calculated Feature: We will engineer the crucial strategic variable Three-Point Attempt Rate (3PAr= 
FGA
3PA
​	
 ) to normalize volume and more accurately represent a team's offensive philosophy.
These two datasets will be merged using `Team` and `Year` as composite keys, creating a single, enriched dataset for analysis.


2.3. Data Acquisition and Processing Plan

The data acquisition and preparation process will be executed in the following steps:

1.  Data Scraping:  Python's `pandas` library (specifically the `read_html()` function) will be used to scrape the "Per Game Stats" and "Advanced" tables for each NBA season from 2000-2001 to 2024-2025.

2.  Data Cleaning: The raw scraped data will be cleaned. This includes removing non-team rows (e.g., "League Average"), standardizing team names (e.g., removing asterisks), and converting statistical columns to the appropriate numeric data types.

3.  Data Merging (Enrichment): The cleaned "Per Game" and "Advanced" DataFrames will be merged into a single DataFrame on the `Team` and `Year` keys.

4.  Data Storage: The final, cleaned, and enriched dataset will be saved as a `.csv` file within this repository's `/data` directory to ensure reproducibility.




1. Data Acquisition and Preparation

This phase establishes the project's panel data structure and involves rigorous preparation to ensure the dataset is robust for statistical modeling.

1.1. Data Sourcing and Retrieval
Data will be programmatically sourced from Basketball-Reference.com, a validated repository for NBA statistics. The primary method will involve utilizing **Python's `pandas.read_html()`** function within an iterative loop spanning the 2000-01 to 2024-25 seasons to retrieve the three necessary, distinct table types (Per Game, Advanced, Shooting). The data will be initially concatenated into three large, separate DataFrames, indexed by season year.

1.2. Data Cleaning and Integration
Standardization: Non-team entries (e.g., "League Average") and non-numeric characters (e.g., the playoff asterisk `*`) will be systematically removed from the `Team` identifier column to ensure consistent keys. Data Coercion: All statistical metrics (`Pace`, `3PA`, `eFG%`) will be explicitly converted to appropriate floating-point numeric types to prevent computational errors. Panel Construction: The three initial DataFrames will be merged via an inner join using the composite key of `Team` and `Year`. This integration results in a balanced panel dataset suitable for time-series and fixed-effects analysis.

1.3. Feature Engineering
To accurately quantify a team's strategic preference, a new predictor variable, the Three-Point Attempt Rate (`3PAr`), will be calculated:
The Three-Point Attempt Rate ($\text{3PAr}$) is the proportion of a team's total field goal attempts ($\text{FGA}$) that are three-point shots ($\text{3PA}$).
This engineered feature is superior to raw volume (`3PA`) as it normalizes attempts relative to total field goal volume.

---

2. Exploratory Data Analysis (EDA) & Visualization 

EDA serves to validate data integrity, characterize variable distributions, and provide preliminary visual evidence for the stated hypotheses. `Matplotlib` and `Seaborn` will be used for high-quality visualization.

2.1. Distribution and Univariate Analysis
Diagnostics: Histograms and Box Plots will be generated for key continuous variables (`Pace`, `3PAr`) to assess normality, identify potential skewness, and flag statistical outliers that may require specific handling (e.g., Winsorizing or investigation). Summary Statistics: Full descriptive statistics (mean, median, standard deviation, etc.) will be calculated across the entire panel.

2.2. Trend and Relationship Visualization
Longitudinal Decomposition (RQ1): The league-average time series for both `Pace` and `3PA` will be plotted on a dual-axis line graph. This visualization will confirm the co-evolutionary trend and allow for visual inspection of the periods where the two variables experienced the steepest increases.  Core Relationship Plot (RQ2): A team-level Scatter Plot will illustrate the relationship between the predictor (`3PAr`) and the dependent variable (`Pace`), including a linear regression trend line to visually confirm the hypothesized positive correlation.

3PA vs Pace Relationship

Scatter plot shows clear positive relationship
More three-point attempts = faster pace
Correlation: r = 0.64, p < 0.001 (strong and significant)

Interpretation:
Teams that shoot more threes play faster. The trend line shows this relationship is consistent across all teams and years. This confirms our hypothesis about the "Pace and Space" connection.

Pace vs Winning Percentage

Scatter plot shows weak relationship
Correlation: r = 0.12, p = 0.08 (not significant)
Points are scattered everywhere - no clear pattern

Interpretation:
Pace alone doesn't predict winning. Both fast and slow teams can win or lose. What matters is efficiency (eFG%), not tempo. You can win playing fast or slow, as long as you shoot well.

---

3. Hypothesis Testing and Preliminary Modeling

This phase provides the initial statistical evidence needed to support the project's core claims using fundamental statistical tools.

3.1. Correlation and Significance Testing
Pearson Correlation: The Pearson product-moment correlation coefficient ($r$) will be calculated for the relationship between `Pace` and `3PAr`. Statistical Significance: A two-tailed hypothesis test will be conducted (using `scipy.stats.pearsonr`) to determine the p-value associated with the correlation. A finding of p < 0.05 will confirm the initial statistically significant relationship between the variables.

3.2. Simple Ordinary Least Squares (OLS) Model
Model Formulation:** A foundational Simple Linear Regression (OLS) model will be constructed using the `statsmodels` library to quantify the isolated impact of the strategic three-point rate on tempo:
The Simple Linear Regression (OLS) model establishes a relationship where a team's Pace is determined by a base constant ($\beta_0$) plus the incremental effect ($\beta_1$) of its Three-Point Attempt Rate (\text{3PAr}), with any unexplained variation accounted for by the error term ($\epsilon$).
Interpretation: The focus will be on the sign and magnitude of the \beta_1 coefficient (expected to be positive) and its associated $p$-value, providing the first numerical evidence for the predictive power of `3PAr` on `Pace`.

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np
import matplotlib.pyplot as plt

4.1 Applying ML Modells.

# 1. Pace Prediction Model
X = df[['3PA', '2PA', 'FTA']]
y = df['Pace']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("=== PACE PREDICTION MODEL ===")
print(f"R² Score: {r2_score(y_test, y_pred):.3f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.3f}")
print(f"\nKatsayılar:")
print(f"3PA: {model.coef_[0]:.3f}")
print(f"2PA: {model.coef_[1]:.3f}")
print(f"FTA: {model.coef_[2]:.3f}")

# 2. Görselleştirme
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel('Actual Pace')
plt.ylabel('Predicted Pace')
plt.title('Pace Model Performance')

# 3. Winning Percentage Model
X_win = df[['Pace', 'eFG%']]
y_win = df['W_PCT']

model2 = LinearRegression()
model2.fit(X_win, y_win)
y_win_pred = model2.predict(X_win)

print("\n=== WINNING PERCENTAGE MODEL ===")
print(f"R² Score: {model2.score(X_win, y_win):.3f}")
print(f"Pace katsayısı: {model2.coef_[0]:.3f}")
print(f"eFG% katsayısı: {model2.coef_[1]:.3f}")

plt.subplot(1, 2, 2)
plt.scatter(y_win, y_win_pred, alpha=0.5)
plt.plot([y_win.min(), y_win.max()], [y_win.min(), y_win.max()], 'r--')
plt.xlabel('Actual Win%')
plt.ylabel('Predicted Win%')
plt.title('Win% Model Performance')

plt.tight_layout()
plt.show()
