import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib as mpl
from scipy.interpolate import griddata
import pandas as pd
data = pd.read_csv('SONTRAC_pixeledplusx.dat',sep='\s+',header=None)
plt.figure(figsize=(13,13), dpi=100)
mpl.rcParams['text.usetex'] = True
mpl.rcParams['axes.linewidth'] = 1.5
plt.rc("font", size=25, family="Arial", weight='bold')
z = data[3]
y = data[2]

# Define number of bins (adjust as needed - renormalize according to frequency counts)
num_bins1 = 20
num_bins2 = 20
# Calculate 2D histogram (frequency counts)
freq, zedges, yedges = np.histogram2d(z, y, bins=(num_bins1,num_bins2))

# Calculate centers of bins for plotting
zcenters = (zedges[:-1] + zedges[1:]) / 2
ycenters = (yedges[:-1] + yedges[1:]) / 2
Z, Y = np.meshgrid(zcenters, ycenters)

# Make contour plot
contour = plt.contourf(Z, Y, freq.T, levels=14, cmap='rainbow', extent=(-2.5, 2.5, -1.4, 1.4))
# Adjust the number of ticks on the pixel plot
plt.locator_params(axis='x', nbins=10)
plt.locator_params(axis='y', nbins=10)
color_bar_ticks=[0, 1000, 2000, 3000, 4000, 5000, 6000, 7000]
colorbar = plt.colorbar(contour, shrink=0.525, ticks=color_bar_ticks)  # Adjust the number of ticks here
colorbar.ax.set_title(r'Frequency')
plt.minorticks_on()
plt.tick_params(axis='both', which='major', length=15, width=2,labelsize=22)
plt.tick_params(axis='both', which='minor', length=7.5, width=1.5,labelsize=22)
plt.xlabel(r'\bf Horizontal distance [cm]', fontsize=27)
plt.ylabel(r'\bf Vertical distance [cm]', fontsize=27)
plt.title(r"(a) Pixelated photo-sensor I", y=1.025)
plt.savefig("Contour_plot_plusx.pdf", bbox_inches='tight')
plt.show()
