import polars as pl

# ========== CONFIGURATION ==========
dataset_path = "2024_fb_ads_president_scored_anon.csv"   # <--- CHANGE FILENAME HERE

# ========== MAIN ANALYSIS ==========
df = pl.read_csv(dataset_path)
print("\n=== OVERALL DESCRIPTIVE STATISTICS ===")
print(df.describe())

for col in df.columns:
    print(f"\nValue counts for {col}:")
    print(df[col].value_counts().head(5))

# GROUP BY page_id
print("\n=== GROUPED BY page_id ===")
numeric_cols = [c for c in df.columns if df[c].dtype in [pl.Float64, pl.Int64]]
if numeric_cols:
    agg_exprs = [pl.col(c).mean().alias(f'{c}_mean') for c in numeric_cols]
    print(df.group_by('page_id').agg(agg_exprs))

# GROUP BY page_id and ad_id
print("\n=== GROUPED BY page_id AND ad_id ===")
if numeric_cols:
    agg_exprs = [pl.col(c).mean().alias(f'{c}_mean') for c in numeric_cols]
    print(df.group_by(['page_id', 'ad_id']).agg(agg_exprs))
