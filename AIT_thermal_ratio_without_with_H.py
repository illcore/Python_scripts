import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Read the data
data1 = pd.read_csv('Bulk_surface_neutron_without_H_1_6_energies_below_1eV.txt', sep='\s+', header=None)
data2 = pd.read_csv('Bulk_surface_neutron_with_H_1_6_energies_below_1eV.txt', sep='\s+', header=None)
data3 = pd.read_csv('Bulk_surface_neutron_without_H_1_93_energies_below_1eV.txt', sep='\s+', header=None)
data4 = pd.read_csv('Bulk_surface_neutron_with_H_1_93_energies_below_1eV.txt', sep='\s+', header=None)

# Set up plot aesthetics
plt.figure(figsize=(13, 13), dpi=100)
mpl.rcParams['text.usetex'] = True
mpl.rcParams['axes.linewidth'] = 1.5
plt.rc("font", size=25, family="Arial", weight='bold')

# Define the bins
bins=np.arange(0, 1, 10e-4)

# Extract data
x1 = data1[0]
x2 = data2[0]
x3 = data3[0]
x4 = data4[0]

# Compute histograms
counts1, _ = np.histogram(x1, bins=bins)
counts2, _ = np.histogram(x2, bins=bins)
counts3, _ = np.histogram(x3, bins=bins)
counts4, _ = np.histogram(x4, bins=bins)

# Calculate the ratio of counts, handling division by zero
nonzero1 = (counts1 != 0) & (counts2 != 0)
bins_nonzero1 = bins[:-1][nonzero1]
ratio_nonzero1 = counts1[nonzero1] / counts2[nonzero1]
nonzero2 = (counts3 != 0) & (counts4 != 0)
bins_nonzero2 = bins[:-1][nonzero2]
ratio_nonzero2 = counts3[nonzero2] / counts4[nonzero2]

# Plot the ratio versus bins
plt.plot(bins_nonzero1, ratio_nonzero1, color='red', linewidth=1.5, label=r"Bulk density=1.6 g/cm$^{3}$", drawstyle='steps')
plt.plot(bins_nonzero2, ratio_nonzero2, color='blue', linewidth=1.5, label=r"Bulk density=1.93 g/cm$^{3}$", drawstyle='steps')

# Ticks
plt.minorticks_on()
plt.tick_params(axis='both', which='major', length=15, width=2, labelsize=22)
plt.tick_params(axis='both', which='minor', length=7.5, width=1.5, labelsize=22)
# Axes limits
plt.xlim(10e-4, 1)
plt.ylim(10e-3, 10e1)
plt.xscale("log")
plt.yscale("log")
plt.title(r'(a)', y=1.025)
plt.legend(frameon=False,shadow=False)
# Axes labels
plt.xlabel(r"\bf Kinetic energy of albedo neutrons [eV]", fontsize=27)
plt.ylabel(r"\bf Ratio of albedo neutrons (without/with $0.1\%$ H)", fontsize=27)

# Save the plot
plt.savefig("Thermal_ratio_bulk.pdf", bbox_inches='tight')
plt.show()
