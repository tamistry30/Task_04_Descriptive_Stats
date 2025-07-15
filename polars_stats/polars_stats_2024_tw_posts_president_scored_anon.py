import polars as pl

filename = "2024_tw_posts_president_scored_anon.csv"
df = pl.read_csv(filename)

print("\n=== First 3 Rows ===")
print(df.head(3))

print("\n=== OVERALL DESCRIPTIVE STATISTICS ===")
print(df.describe())

# Get numeric columns
numeric_cols = [col for col, dtype in zip(df.columns, df.dtypes) if dtype in [pl.Int64, pl.Float64, pl.UInt32, pl.UInt64]]

# Only aggregate numeric columns
if 'lang' in df.columns:
    print("\n=== GROUPED BY lang (numeric columns only) ===")
    grouped = df.group_by('lang').agg(
        [pl.col(col).mean().alias(f'{col}_mean') for col in numeric_cols] +
        [pl.col(col).min().alias(f'{col}_min') for col in numeric_cols] +
        [pl.col(col).max().alias(f'{col}_max') for col in numeric_cols] +
        [pl.col(col).count().alias(f'{col}_count') for col in numeric_cols]
    )
    print(grouped.head(10))

# Grouped by month_year (numeric columns only)
if 'month_year' in df.columns:
    print("\n=== GROUPED BY month_year (numeric columns only) ===")
    grouped = df.group_by('month_year').agg(
        [pl.col(col).mean().alias(f'{col}_mean') for col in numeric_cols] +
        [pl.col(col).min().alias(f'{col}_min') for col in numeric_cols] +
        [pl.col(col).max().alias(f'{col}_max') for col in numeric_cols] +
        [pl.col(col).count().alias(f'{col}_count') for col in numeric_cols]
    )
    print(grouped.head(10))
