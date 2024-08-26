import pandas as pd
data3 = pd.read_csv('Concrete_steel_angle_average.txt',sep='\s+',header=None)
data4 = pd.read_csv('Concrete_steel_Co_angle_average.txt',sep='\s+',header=None)
data5 = pd.read_csv('Concrete_steel_Sr_angle_average.txt',sep='\s+',header=None)
data6 = pd.read_csv('Concrete_steel_Cs_angle_average.txt',sep='\s+',header=None)
data7 = pd.read_csv('Concrete_steel_uranium_angle_average.txt',sep='\s+',header=None)
data8 = pd.read_csv('Concrete_steel_Pu_angle_average.txt',sep='\s+',header=None)
from scipy.optimize import curve_fit
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.figure(figsize=(13,13), dpi=100)
mpl.rcParams['text.usetex'] = True
mpl.rcParams['axes.linewidth'] = 1.5
plt.rc("font", size=25, family="Arial", weight='bold')
x3 = data3[0]
y3 = data3[2] 
x4 = data4[0]
y4 = data4[2]
x5 = data5[0]
y5 = data5[2]
x6 = data6[0]
y6 = data6[2]
x7 = data7[0]
y7 = data7[2]
x8 = data8[0]
y8 = data8[2]
yerr3=data3[3]
yerr4=data4[3]
yerr5=data5[3]
yerr6=data6[3]
yerr7=data7[3]
yerr8=data8[3]
plt.plot(x3,y3, color='Yellow', label=r'\bf Waste barrel',linewidth=1.5)
plt.errorbar(x3, y3, yerr3, solid_capstyle='projecting',linewidth=2, capsize=8, fmt=".", color='Yellow', label=None)
plt.plot(x4,y4, color='MediumBlue', label=r'\bf Waste barrel+cobalt',linewidth=1.5)
plt.errorbar(x4, y4, yerr4, solid_capstyle='projecting',linewidth=2, capsize=8, fmt=".", color='MediumBlue', label=None)
plt.plot(x5,y5, color='Orange', label=r'\bf Waste barrel+strontium',linewidth=1.5)
plt.errorbar(x5, y5, yerr5, solid_capstyle='projecting',linewidth=2, capsize=8, fmt=".", color='Orange', label=None)
plt.plot(x6,y6, color='Purple', label=r'\bf Waste barrel+caesium',linewidth=1.5)
plt.errorbar(x6, y6, yerr6, solid_capstyle='projecting',linewidth=2, capsize=8, fmt=".", color='Purple', label=None)
plt.plot(x7,y7, color='Pink', label=r'\bf Waste barrel+uranium',linewidth=1.5)
plt.errorbar(x7, y7, yerr7, solid_capstyle='projecting',linewidth=2, capsize=8, fmt=".", color='Pink', label=None)
plt.plot(x8,y8, color='Lime', label=r'\bf Waste barrel+plutonium',linewidth=1.5)
plt.errorbar(x8, y8, yerr8, solid_capstyle='projecting',linewidth=2, capsize=8, fmt=".", color='Lime', label=None)
# Ticks
plt.minorticks_on()
plt.tick_params(axis='both', which='major', length=15, width=2,labelsize=22)
plt.tick_params(axis='both', which='minor', length=7.5, width=1.5,labelsize=22)
plt.xticks(np.arange(0.5, 8.01, step=0.5))
plt.yticks(np.arange(0, 501, step=25))
#Axes limits
plt.xlim(0.5, 8.01)
plt.ylim(0.0, 500.01)
#Axes labels
plt.xlabel(r"\bf Initial kinetic energy [GeV]", fontsize=27)
plt.ylabel(r"\bf Average scattering angle [mrad]", fontsize=27)
#No legend frame and shadow
plt.legend(frameon=False,shadow=False)
plt.savefig("Scattering_angle_05.pdf", bbox_inches='tight')
plt.show()
