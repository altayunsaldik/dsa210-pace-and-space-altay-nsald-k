import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# 1. Loading the Enriched Dataset
# Assuming 'nba_enriched.csv' is your merged panel data [cite: 33]
df = pd.read_csv('data/nba_enriched.csv')

# 2. Summary Statistics & Data Integrity Check
print("--- Descriptive Statistics ---")
print(df[['Pace', '3PA', '3PAr', 'eFG%', 'W_PCT']].describe())

# Check for missing values 
print("\nMissing Values:\n", df.isnull().sum())

# 3. Univariate Analysis: Distributions
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(df['Pace'], kde=True, color='orange')
plt.title('Distribution of Game Pace (2000-2025)')

plt.subplot(1, 2, 2)
sns.histplot(df['3PAr'], kde=True, color='blue')
plt.title('Distribution of 3-Point Attempt Rate')
plt.show()

# 4. Bivariate Analysis: Correlation Heatmap [cite: 12]
plt.figure(figsize=(10, 8))
correlation_matrix = df[['Pace', '3PA', '3PAr', 'eFG%', 'W_PCT', 'FTA']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Feature Correlation Heatmap')
plt.show()

# 5. Hypothesis Testing (RQ2: Pace vs. 3PAr) 
# Null Hypothesis (H0): There is no correlation between 3PAr and Pace.
r_val, p_val = stats.pearsonr(df['3PAr'], df['Pace'])

print(f"--- Hypothesis Test Results ---")
print(f"Pearson Correlation Coefficient: {r_val:.4f}")
print(f"P-Value: {p_val:.4e}")

if p_val < 0.05:
    print("Result: Reject H0. Significant relationship exists between 3PAr and Pace.")
else:
    print("Result: Fail to reject H0.")

# 6. Identifying Outliers (Boxplot) 
plt.figure(figsize=(8, 4))
sns.boxplot(x='Pace', data=df)
plt.title('Identifying Pace Outliers')
plt.show()
