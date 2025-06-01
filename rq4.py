import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('RQ4.CSV')

# Step 1: Count selections
line_counts = df[df['VALUE'] == 'L']['LINE'].value_counts()
column_counts = df[df['VALUE'] == 'C']['COLLUMN'].value_counts()

# Step 2: Combine and fill missing with 0
combined_counts = line_counts.add(column_counts, fill_value=0)

# Step 3: Normalize counts to simulate AHP weights
total = combined_counts.sum()
ahp_weights = combined_counts / total

# Step 4: Sort by weight
ahp_ranking = ahp_weights.sort_values(ascending=False)

# Step 5: Create DataFrame for inspection
ahp_df = pd.DataFrame({
    'Attribute': ahp_ranking.index,
    'AHP_Weight': ahp_ranking.values,
    'Total_Count': combined_counts[ahp_ranking.index].values
})

# Step 6: Plot with no space between bars
colors = plt.cm.tab20.colors[:len(ahp_ranking)]

plt.figure(figsize=(10, 5))
plt.bar(ahp_ranking.index, ahp_ranking.values, color=colors, width=1.0)
plt.title('AHP Ranking of Software Quality Attributes')
plt.xlabel('Attribute (LINE or COLLUMN)')
plt.ylabel('Normalized AHP Weight')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Optional: print ranking
print(ahp_df.to_string(index=False))
