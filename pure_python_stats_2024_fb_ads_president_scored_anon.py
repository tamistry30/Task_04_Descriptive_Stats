import csv
import math
from collections import Counter, defaultdict

# ========== CONFIGURATION ==========
dataset_path = "2024_fb_ads_president_scored_anon.csv"   # <--- CHANGE FILENAME HERE

# ========== HELPER FUNCTIONS ==========
def is_float(val):
    try:
        float(val)
        return True
    except:
        return False

def mean(lst):
    lst = [float(x) for x in lst]
    return sum(lst) / len(lst) if lst else float('nan')

def stddev(lst):
    m = mean(lst)
    lst = [float(x) for x in lst]
    return math.sqrt(sum((x - m) ** 2 for x in lst) / len(lst)) if len(lst) > 1 else 0.0

def describe_column(values): 
    numeric = [float(v) for v in values if is_float(v)]
    non_numeric = [v for v in values if not is_float(v)]
    desc = {}
    if numeric:
        desc['count'] = len(numeric)
        desc['mean'] = mean(numeric)
        desc['min'] = min(numeric)
        desc['max'] = max(numeric)
        desc['std'] = stddev(numeric)
    if non_numeric or not numeric:
        desc['unique'] = len(set(values))
        desc['top'] = Counter(values).most_common(1)[0][0]
        desc['freq'] = Counter(values).most_common(1)[0][1]
    return desc

# ========== MAIN ANALYSIS ==========
with open(dataset_path, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    columns = reader.fieldnames
    
    if columns is None:
        # Try to read the first row to initialize fieldnames
        try:
            first_row = next(reader)
            columns = reader.fieldnames
            if columns is None:
                # If still None, use keys from first row
                columns = list(first_row.keys())
            rows = [first_row]
        except StopIteration:
            raise ValueError("CSV file is empty or missing header row.")
    else:
        rows = []
    
    # Ensure columns is not None
    if columns is None:
        raise ValueError("Could not determine column names from CSV file.")
    
    data = {col: [] for col in columns}
    
    # Add first row data if we read it above
    if rows:
        for col in columns:
            data[col].append(rows[0][col])
    
    # Read remaining rows
    for row in reader:
        rows.append(row)
        for col in columns:
            data[col].append(row[col])

print("\n=== OVERALL DESCRIPTIVE STATISTICS ===")
for col in columns:
    print(f"\nColumn: {col}")
    stats = describe_column(data[col])
    for k, v in stats.items():
        print(f"  {k}: {v}")

# GROUP BY page_id
print("\n=== GROUPED BY page_id ===")
groups = defaultdict(list)
for row in rows:
    groups[row['page_id']].append(row)
for group, group_rows in groups.items():
    print(f"\nGroup: page_id = {group}")
    group_data = {col: [r[col] for r in group_rows] for col in columns}
    for col in columns:
        stats = describe_column(group_data[col])
        print(f"  Column: {col}")
        for k, v in stats.items():
            print(f"    {k}: {v}")

# GROUP BY page_id and ad_id
print("\n=== GROUPED BY page_id AND ad_id ===")
groups2 = defaultdict(list)
for row in rows:
    groups2[(row['page_id'], row['ad_id'])].append(row)
for group, group_rows in list(groups2.items())[:10]:  # Show only first 10 for brevity
    print(f"\nGroup: page_id = {group[0]}, ad_id = {group[1]}")
    group_data = {col: [r[col] for r in group_rows] for col in columns}
    for col in columns:
        stats = describe_column(group_data[col])
        print(f"  Column: {col}")
        for k, v in stats.items():
            print(f"    {k}: {v}")
