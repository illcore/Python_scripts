import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib as mpl
# Initialize a 34x34 matrix with zeros
pixel_matrix = [[0 for _ in range(34)] for _ in range(34)]

# Read the output file
with open("output_pixeledplusx.txt", "r") as file:
    # Loop over each line in the file
    for line in file:
        # Split the line into pixel copy number and hit value
        pixel_number, hit_value = map(int, line.split())
        # Calculate the row and column index from the pixel copy number
        row = math.floor((pixel_number - 1)/34)
        column = (pixel_number - 1) % 34
        # Assign the hit value to the corresponding cell in the matrix
        pixel_matrix[row][column] = hit_value

pixel_matrix.reverse()
# Convert the pixel matrix to a numpy array for plotting
pixel_array = np.array(pixel_matrix)
# Create a pixel plot using Matplotlib
plt.figure(figsize=(13,13), dpi=100)
mpl.rcParams['text.usetex'] = True
mpl.rcParams['axes.linewidth'] = 1.5
plt.rc("font", size=25, family="Arial", weight='bold')
plt.imshow(pixel_array, cmap='viridis', interpolation='nearest', extent=(-2.5, 2.5, -2.5, 2.5))

# Adjust the number of ticks on the pixel plot
plt.locator_params(axis='x', nbins=10)
plt.locator_params(axis='y', nbins=10)
colorbar = plt.colorbar()
colorbar.ax.set_title(r'Hits')
plt.xlabel(r'\bf Horizontal distance [cm]', fontsize=27)
plt.ylabel(r'\bf Vertical distance [cm]', fontsize=27)
plt.minorticks_on()
plt.tick_params(axis='both', which='major', length=15, width=2,labelsize=22)
plt.tick_params(axis='both', which='minor', length=7.5, width=1.5,labelsize=22)
plt.title(r"(c) 100-MeV neutron, pixel grid: +x")
plt.savefig("Pixeled_plot_plusx.pdf", bbox_inches='tight')
plt.show()

