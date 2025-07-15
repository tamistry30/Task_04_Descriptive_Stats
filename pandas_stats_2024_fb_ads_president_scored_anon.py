import pandas as pd

# ========== CONFIGURATION ==========
dataset_path = "2024_fb_ads_president_scored_anon.csv"   # <--- CHANGE FILENAME HERE

# ========== MAIN ANALYSIS ==========
print("Loading data...")
df = pd.read_csv(dataset_path)

# Limit to first 1000 rows for faster processing
df = df.head(1000)

print(f"\nDataset shape: {df.shape}")
print("\n=== OVERALL DESCRIPTIVE STATISTICS ===")
print(df.describe(include='all'))

print("\n=== COLUMN OVERVIEW ===")
for col in df.columns:
    print(f"\n{col}:")
    print(f"  Unique values: {df[col].nunique()}")
    print(f"  Top 3 values: {df[col].value_counts().head(3).to_dict()}")

# GROUP BY page_id (limited to first 5 groups)
print("\n=== GROUPED BY page_id (first 5 groups) ===")
grouped = df.groupby('page_id')
for i, (page_id, group) in enumerate(grouped):
    if i >= 5:  # Only show first 5 groups
        break
    print(f"\npage_id = {page_id} (rows: {len(group)})")
    print(group.describe())

print(f"\nTotal unique page_ids: {df['page_id'].nunique()}")

#