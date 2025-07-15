import pandas as pd

filename = "2024_fb_posts_president_scored_anon.csv"
df = pd.read_csv(filename)

print("\n=== First 3 Rows ===")
print(df.head(3))

print("\n=== OVERALL DESCRIPTIVE STATISTICS ===")
print(df.describe(include='all'))  # Removed datetime_is_numeric=True

for col in df.columns:
    print(f"\nValue counts for {col}:")
    print(df[col].value_counts(dropna=False).head(5))

# Only use numeric columns for grouping
numeric_cols = df.select_dtypes(include='number').columns

print("\n=== GROUPED BY Facebook_Id (numeric columns only) ===")
print(df.groupby('Facebook_Id')[numeric_cols].agg(['count', 'mean', 'min', 'max']).head(5))

print("\n=== GROUPED BY Facebook_Id AND post_id (numeric columns only) ===")
print(df.groupby(['Facebook_Id', 'post_id'])[numeric_cols].agg(['count', 'mean', 'min', 'max']).head(5))
