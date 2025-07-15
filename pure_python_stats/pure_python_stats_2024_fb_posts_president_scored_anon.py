import csv
import math
from collections import Counter, defaultdict

filename = "2024_fb_posts_president_scored_anon.csv"

def is_float(val):
    try:
        float(val)
        return True
    except:
        return False

def mean(lst):
    lst = [float(x) for x in lst if is_float(x)]
    return sum(lst) / len(lst) if lst else float('nan')

def stddev(lst):
    m = mean(lst)
    lst = [float(x) for x in lst if is_float(x)]
    return math.sqrt(sum((x - m) ** 2 for x in lst) / len(lst)) if len(lst) > 1 else 0.0

def describe_column(values):
    numeric = [float(v) for v in values if is_float(v)]
    desc = {}
    if numeric:
        desc['count'] = len(numeric)
        desc['mean'] = mean(numeric)
        desc['min'] = min(numeric)
        desc['max'] = max(numeric)
        desc['std'] = stddev(numeric)
    else:
        desc['unique'] = len(set(values))
        desc['top'] = Counter(values).most_common(1)[0][0]
        desc['freq'] = Counter(values).most_common(1)[0][1]
    return desc

with open(filename, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    columns = reader.fieldnames
    data = {col: [] for col in columns}
    rows = []
    for row in reader:
        rows.append(row)
        for col in columns:
            data[col].append(row[col])

print("\n=== First 3 Rows ===")
for r in rows[:3]:
    print(r)

print("\n=== OVERALL DESCRIPTIVE STATISTICS ===")
for col in columns:
    print(f"\nColumn: {col}")
    stats = describe_column(data[col])
    for k, v in stats.items():
        print(f"  {k}: {v}")

# GROUP BY Facebook_Id (page)
print("\n=== GROUPED BY Facebook_Id ===")
groups = defaultdict(list)
for row in rows:
    if 'Facebook_Id' in row:
        groups[row['Facebook_Id']].append(row)
for group, group_rows in list(groups.items())[:3]:  # Show first 3 groups for brevity
    print(f"\nGroup: Facebook_Id = {group}")
    group_data = {col: [r[col] for r in group_rows] for col in columns}
    for col in columns:
        stats = describe_column(group_data[col])
        print(f"  Column: {col}")
        for k, v in stats.items():
            print(f"    {k}: {v}")

# GROUP BY Facebook_Id and post_id
print("\n=== GROUPED BY Facebook_Id AND post_id ===")
groups2 = defaultdict(list)
for row in rows:
    if 'Facebook_Id' in row and 'post_id' in row:
        groups2[(row['Facebook_Id'], row['post_id'])].append(row)
for group, group_rows in list(groups2.items())[:3]:  # Show first 3 for preview
    print(f"\nGroup: Facebook_Id = {group[0]}, post_id = {group[1]}")
    group_data = {col: [r[col] for r in group_rows] for col in columns}
    for col in columns:
        stats = describe_column(group_data[col])
        print(f"  Column: {col}")
        for k, v in stats.items():
            print(f"    {k}: {v}")
