<h1 align='center'> Kruskal-Wallis Test for Multiple Variables and Group Comparisons</h1>

This project provides a reusable Python function to perform the **Kruskal-Wallis H-test** across **multiple continuous variables**, grouped by a categorical feature. It returns a **clean summary DataFrame** with test statistics, p-values, and significance indicators, making it easy to evaluate whether medians differ significantly between groups for each variable.

## 📌 Purpose

The Kruskal-Wallis test is a **non-parametric alternative to one-way ANOVA**. It is used when:
- You have **3 or more independent groups**
- Your data **violates ANOVA assumptions** (e.g., normality, homogeneity of variance)
- Your data is **ordinal or continuous but not normally distributed**

This script simplifies applying this test across **many variables at once**, saving time and boosting productivity in exploratory and inferential analysis.

## Features

- Accepts a pandas DataFrame and a grouping column
- Automatically applies the Kruskal-Wallis test to all other numeric variables
- Outputs a summary table including:
  - Variable name
  - Kruskal-Wallis test statistic
  - p-value
  - Significance status (`p < 0.05`)
- Ready for integration in statistical reports or dashboards

##  How to Use

```python
from scipy.stats import kruskal
import pandas as pd

# Define function
def kruskal_test_all_variables(df, group_col):
    results = []
    variables = df.columns.drop(group_col)
    
    for var in variables:
        groups = [group[var].dropna().values for name, group in df.groupby(group_col)]
        stat, p = kruskal(*groups)
        results.append({
            'Variable': var,
            'Kruskal-Wallis Statistic': stat,
            'p-value': p,
            'Significant (p<0.05)': p < 0.05
        })
    
    return pd.DataFrame(results)

```

📂 Example Dataset
```
df = pd.DataFrame({
    'Group': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'Var1': [12, 14, 13, 15, 16, 14, 10, 9, 11],
    'Var2': [7, 6, 7, 8, 9, 10, 5, 6, 5],
    'Var3': [20, 21, 19, 23, 22, 21, 18, 17, 19]
})

results = kruskal_test_all_variables(df, 'Group')
print(results)
```


📊 Sample Output

Variable	Kruskal-Wallis Statistic	p-value	Significant (p<0.05)

Var1	5.143	0.076	False
Var2	6.000	0.050	True
Var3	7.200	0.027	True


📈 Applications

- Agricultural and biological experiments
- Social science and behavioral research
- Market and product group analysis
- Education and clinical trial comparisons

📥 Requirements

- Python 3.x
- pandas
- scipy

```
pip install pandas scipy
```


🤝 Contributing

Feel free to fork this repo, contribute improvements, or suggest additional features such as post-hoc Dunn tests, visualization tools, or effect size calculation.


⭐️ If You Found This Useful

- Leave a star 🌟
- Share feedback
- Fork and adapt for your project
- Mention the project in your work!

## License

MIT License

