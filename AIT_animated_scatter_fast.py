import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib.animation import FuncAnimation, PillowWriter

# Load data
data = pd.read_csv('SONTRAC_pixeledminusx.dat', sep='\s+', header=None)
x_coords = data[3].values
y_coords = data[2].values
n_points = len(x_coords)

# Control how many points to add per frame (batch size)
step = 1000  # Change this value for larger/smaller batches

# Calculate number of frames needed
frames = np.arange(step, n_points + step, step)
if frames[-1] > n_points:
    frames[-1] = n_points  # Ensure last frame includes all points

# Plotting setup
mpl.rcParams['text.usetex'] = True
mpl.rcParams['axes.linewidth'] = 1.5
plt.rc("font", size=25, family="Arial", weight='bold')

fig, ax = plt.subplots(figsize=(13, 13), dpi=100)
sc = ax.scatter([], [], color='blue', s=5)
ax.minorticks_on()
ax.tick_params(axis='both', which='major', length=15, width=2, labelsize=22)
ax.tick_params(axis='both', which='minor', length=7.5, width=1.5, labelsize=22)
ax.set_xticks(np.arange(-2.501, 2.501, step=0.5))
ax.set_yticks(np.arange(-1.4001, 1.4001, step=0.2))
ax.set_xlim(-2.501, 2.501)
ax.set_ylim(-1.4001, 1.4001)
ax.set_xlabel('Z-coordinate [cm]')
ax.set_ylabel('Y-coordinate [cm]')

def animate(frame_end):
    sc.set_offsets(np.c_[x_coords[:frame_end], y_coords[:frame_end]])
    return sc,

output_filename = "Animated_distribution_on_pixelminusx.gif"
if output_filename.endswith('.gif'):
    anim = FuncAnimation(
        fig, animate, frames=frames, interval=20, blit=True, repeat=False
    )
    anim.save(output_filename, writer=PillowWriter(fps=100))
    
    ax.scatter(x_coords, y_coords, color='blue', s=5)
    plt.savefig("Distribution_on_pixelminusx.pdf", bbox_inches='tight')

plt.show()
