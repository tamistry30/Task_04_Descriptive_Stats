import pandas as pd

filename = "2024_tw_posts_president_scored_anon.csv"
df = pd.read_csv(filename)

print("\n=== First 3 Rows ===")
print(df.head(3))

print("\n=== OVERALL DESCRIPTIVE STATISTICS ===")
print(df.describe(include='all'))

for col in df.columns:
    print(f"\nValue counts for {col}:")
    print(df[col].value_counts(dropna=False).head(5))

# Numeric columns only!
numeric_cols = df.select_dtypes(include='number').columns

print("\n=== GROUPED BY lang (numeric columns only) ===")
print(df.groupby('lang')[numeric_cols].agg(['count', 'mean', 'min', 'max']).head(10))

if 'month_year' in df.columns:
    print("\n=== GROUPED BY month_year (numeric columns only) ===")
    print(df.groupby('month_year')[numeric_cols].agg(['count', 'mean', 'min', 'max']).head(10))
