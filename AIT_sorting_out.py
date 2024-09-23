import pandas as pd
df = pd.read_csv('waste_barrel_U.dat', sep=' ',header=None)
import sympy as sym
import numpy as np
import math
# Create a helper column to maintain the original order
df['original_order'] = range(len(df))

# Sort by the first column while keeping the original order for rows with the same value in the first column
df_sorted = df.sort_values(by=[0, 'original_order'], kind='stable').drop(columns='original_order')

# Write the grouped data to a new file
df_sorted.to_csv("Sorted_waste_barrel_U.dat", index=False, header=False, sep=' ')



