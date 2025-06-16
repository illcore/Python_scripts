import numpy as np
import pandas as pd

# Read only columns 2 (Energy) and 3 (Angle) from your data file
df = pd.read_csv('Linear_perturbation_1_mm_angles.txt', sep=" ", header=None, usecols=[1, 2], names=['Energy', 'Angle'])

# Create 32 bins between 0 and 8.0
n_bins = 32
bin_edges = np.linspace(0, 8.0, n_bins + 1)
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

# Assign bins - Energy in GeV
df['bin'] = pd.cut(df['Energy']/1000, bins=bin_edges, labels=bin_centers, include_lowest=True, right=False)

# Calculate count, mean, std for each bin
grouped = df.groupby('bin')['Angle']
counts = grouped.count().reindex(bin_centers, fill_value=0)
means = grouped.mean().reindex(bin_centers)
stds = grouped.std(ddof=1).reindex(bin_centers)

# Build final DataFrame
out_df = pd.DataFrame({
    'bin_center': bin_centers,
    'count': counts.astype(int),
    'mean': means,
    'std': stds
})

# Replace NaN with empty string for mean and std columns
out_df[['mean', 'std']] = out_df[['mean', 'std']].fillna('')

# Write to output.txt with no header and no index
out_df.to_csv('output.txt', sep=' ', index=False, header=False)
