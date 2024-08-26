import pandas as pd
data1 = pd.read_csv('SONTRAC_pixeledplusx.dat',sep=' ',header=None)
import sympy as sym
import numpy as np
import math
from collections import Counter
c = Counter(list(zip(data1[7])))
print(c)
sorted_items = sorted(c.items(), key=lambda x: x[1], reverse=True)
with open("output_pixeledplusx.txt", "w") as f:
    # Iterate over each key-value pair in the Counter object
    for key, value in sorted_items:
        # Write the key and its count separated by a tab or comma
        f.write(f"{key[0]}\t{value}\n")  # Separate columns by a tab (\t) or comma (,)



