import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# 1. DATA PREPARATION (Simulation)
# Note: In the actual project, use pd.read_html() to fetch data from Basketball-Reference.
np.random.seed(42)
n_teams = 750 # 25 seasons x 30 teams

data = {
    'Year': np.repeat(np.arange(2000, 2025), 30),
    '3PA': np.linspace(13, 35, n_teams) + np.random.normal(0, 3, n_teams),
    'FGA': np.linspace(80, 90, n_teams) + np.random.normal(0, 2, n_teams),
    'Pace': np.linspace(90, 100, n_teams) + np.random.normal(0, 2, n_teams),
    'eFG%': np.random.uniform(0.45, 0.55, n_teams),
    'W_PCT': np.random.uniform(0.20, 0.80, n_teams)
}
df = pd.DataFrame(data)

# Feature Engineering: 3PAr (Three-Point Attempt Rate)
df['3PAr'] = df['3PA'] / df['FGA']

# 2. EXPLORATORY DATA ANALYSIS (EDA)
plt.figure(figsize=(14, 5))

# Longitudinal Trend (RQ1)
plt.subplot(1, 2, 1)
league_avg = df.groupby('Year')[['Pace', '3PA']].mean()
sns.lineplot(data=league_avg['3PA'], color='blue', label='3P Attempts')
ax2 = plt.twinx()
sns.lineplot(data=league_avg['Pace'], color='red', ax=ax2, label='Pace')
plt.title('Evolution of Pace and 3PA Over Time')
plt.xlabel('Season')

# Pace vs 3PAr Relationship (RQ2)
plt.subplot(1, 2, 2)
sns.regplot(x='3PAr', y='Pace', data=df, scatter_kws={'alpha':0.3}, line_kws={'color':'red'})
plt.title('Relationship: 3P Attempt Rate vs. Pace')
plt.xlabel('3PAr (3PA / FGA)')
plt.ylabel('Pace')

plt.tight_layout()
plt.show()

# 3. STATISTICAL MODELING (RQ3 & RQ4)

# Model 1: Predicting Pace based on Shooting Volume
X_pace = df[['3PA']] 
y_pace = df['Pace']

X_train, X_test, y_train, y_test = train_test_split(X_pace, y_pace, test_size=0.2)
pace_model = LinearRegression().fit(X_train, y_train)

# Model 2: Win Percentage (Pace vs. Efficiency)
X_win = df[['Pace', 'eFG%']]
y_win = df['W_PCT']
win_model = LinearRegression().fit(X_win, y_win)

# 4. OUTPUT RESULTS
print(f"--- ANALYTICAL RESULTS ---")
print(f"Correlation between Pace & 3PAr: {df['Pace'].corr(df['3PAr']):.2f}")
print(f"Pace Model R² Score: {pace_model.score(X_test, y_test):.2f}")
print(f"Win Percentage Model - eFG% Coefficient: {win_model.coef_[1]:.4f}")
print(f"Win Percentage Model - Pace Coefficient: {win_model.coef_[0]:.4f}")
