import polars as pl

filename = "2024_fb_posts_president_scored_anon.csv"
df = pl.read_csv(filename)

print("\n=== First 3 Rows ===")
print(df.head(3))

print("\n=== OVERALL DESCRIPTIVE STATISTICS ===")
print(df.describe())

for col in df.columns:
    print(f"\nValue counts for {col}:")
    print(df[col].value_counts().head(5))

print("\n=== GROUPED BY page_id ===")
grouped = df.group_by('Facebook_Id').agg([
    pl.col(c).mean().alias(f'{c}_mean')
    for c in df.columns if df[c].dtype in [pl.Float64, pl.Int64]
])
print(grouped)

print("\n=== GROUPED BY page_id AND post_id ===")
grouped2 = df.group_by(['Facebook_Id', 'post_id']).agg([
    pl.col(c).mean().alias(f'{c}_mean')
    for c in df.columns if df[c].dtype in [pl.Float64, pl.Int64]
])
print(grouped2)
