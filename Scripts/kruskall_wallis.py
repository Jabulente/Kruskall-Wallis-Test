from scipy.stats import kruskal
import pandas as pd
import numpy as np

def kruskall_wallis(df, group_columns: str, numerical_columns: list = None):
    if numerical_columns is None:
        numerical_columns = df.select_dtypes(include=[np.number]).columns.tolist()
        for g in group_columns:
            if g in numerical_columns:
                numerical_columns.remove(g)
    results = []
    for group_column in group_columns:
        for column in numerical_columns:
            # Create a list of samples grouped by group_column
            groups = [group[column].dropna().values for name, group in df.groupby(group_column)]
            stats, p_value = kruskal(*groups)
            interpretation = '✔' if p_value < 0.05 else '✖'
            results.append({
                'Group': group_column,
                'Variables': column,
                'Kruskal-Wallis Statistic': stats,
                'P-value': p_value,
                'Significant (α<0.05)': interpretation
            })
    return pd.DataFrame(results)

# Suppose you have DataFrame like this
df = pd.DataFrame({
    'Group 1': ['Ashura', 'Ashura', 'Ashura', 'Barack', 'Barack', 'Barack', 'Colins', 'Colins', 'Colins'],
    'Group 2': ['Orenge', 'Orenge', 'Orenge', 'Banana', 'Banana', 'Banana', 'Carott', 'Carott', 'Carott'],
    'Group 3': ['Alpha', 'Alpha', 'Alpha', 'Bravo', 'Bravo', 'Bravo', 'Eagle', 'Eagle', 'Eagle'],
    'Variable 1': [12, 14, 13, 15, 16, 14, 10, 9, 11],
    'Variable 2': [7, 6, 7, 8, 9, 10, 5, 6, 5],
    'Variable 3': [20, 21, 19, 23, 22, 21, 18, 17, 19],
    'Variable 4': [124, 145, 137, 150, 163, 148, 180, 90, 111],
    'Variable 5': [70, 66, 75, 80, 92, 100, 56, 64, 56],
    'Variable 6': [2, 2, 1, 2, 2, 2, 1, 1, 1]
})

# Perform Kruskal-Wallis Test on all variables by group
group_columns = ['Group 1', 'Group 2', 'Group 3']                   # List of categorical columns or factors
numerical_columns = df.select_dtypes(include=[np.number]).columns   # List of numerical variables
results = kruskall_wallis(df, group_columns, numerical_columns)     # Perform test Kruskall Wallis Test
pd.set_option('display.float_format', lambda x: '%.4f' % x)         # Display Configuration
display(results)