<h1 align='center'> Kruskal-Wallis Test for Multiple Variables and Group Comparisons</h1>

This project provides a reusable Python function to perform the **Kruskal-Wallis H-test** across **multiple continuous variables**, grouped by a categorical feature. It returns a **clean summary DataFrame** with test statistics, p-values, and significance indicators, making it easy to evaluate whether medians differ significantly between groups for each variable.

## 1. Purpose

The Kruskal-Wallis test is a **non-parametric alternative to one-way ANOVA**. It is used when:
- You have **3 or more independent groups**
- Your data **violates ANOVA assumptions** (e.g., normality, homogeneity of variance)
- Your data is **ordinal or continuous but not normally distributed**

This script simplifies applying this test across **many variables at once**, saving time and boosting productivity in exploratory and inferential analysis.

## 2. Features

- Accepts a pandas DataFrame and a grouping column
- Automatically applies the Kruskal-Wallis test to all other numeric variables
- Outputs a summary table including:
  - Variable name
  - Kruskal-Wallis test statistic
  - p-value
  - Significance status (`p < 0.05`)
- Ready for integration in statistical reports or dashboards

##  3. How to Use

```python
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

```

## 4. 📂 Example Dataset
```
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


groups_column = ['Group 1', 'Group 2', 'Group 3']
results = kruskal_test_all_variables(df, 'Group')
print(results)
```


##  5. Sample Output

Variable	Kruskal-Wallis Statistic	p-value	Significant (p<0.05)

|    | Group   | Variables   |   Kruskal-Wallis Statistic |   P-value | Significant (α<0.05)   |
|---:|:--------|:------------|---------------------------:|----------:|:-----------------------|
|  0 | Group 1 | Variable 1  |                      6.88  |     0.032 | ✔                      |
|  1 | Group 1 | Variable 2  |                      6.997 |     0.03  | ✔                      |
|  2 | Group 1 | Variable 3  |                      6.531 |     0.038 | ✔                      |
|  3 | Group 1 | Variable 4  |                      2.4   |     0.301 | ✖                      |
|  4 | Group 1 | Variable 5  |                      7.261 |     0.027 | ✔                      |
|  5 | Group 1 | Variable 6  |                      5.6   |     0.061 | ✖                      |
|  6 | Group 2 | Variable 1  |                      6.88  |     0.032 | ✔                      |
|  7 | Group 2 | Variable 2  |                      6.997 |     0.03  | ✔                      |
|  8 | Group 2 | Variable 3  |                      6.531 |     0.038 | ✔                      |
|  9 | Group 2 | Variable 4  |                      2.4   |     0.301 | ✖                      |
| 10 | Group 2 | Variable 5  |                      7.261 |     0.027 | ✔                      |
| 11 | Group 2 | Variable 6  |                      5.6   |     0.061 | ✖                      |
| 12 | Group 3 | Variable 1  |                      6.88  |     0.032 | ✔                      |
| 13 | Group 3 | Variable 2  |                      6.997 |     0.03  | ✔                      |
| 14 | Group 3 | Variable 3  |                      6.531 |     0.038 | ✔                      |
| 15 | Group 3 | Variable 4  |                      2.4   |     0.301 | ✖                      |
| 16 | Group 3 | Variable 5  |                      7.261 |     0.027 | ✔                      |
| 17 | Group 3 | Variable 6  |                      5.6   |     0.061 | ✖                      |

# 6. 📈 Applications

- Agricultural and biological experiments
- Social science and behavioral research
- Market and product group analysis
- Education and clinical trial comparisons

## 7. 📥 Requirements

- Python 3.x
- pandas
- scipy

```
pip install pandas scipy
```


## 8. 🤝 Contributing

Feel free to fork this repo, contribute improvements, or suggest additional features such as post-hoc Dunn tests, visualization tools, or effect size calculation.


⭐️ If You Found This Useful

- Leave a star 🌟
- Share feedback
- Fork and adapt for your project
- Mention the project in your work!

## 9. License

MIT License

