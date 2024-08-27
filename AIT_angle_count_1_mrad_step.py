import pandas as pd
data3 = pd.read_csv('Concrete_steel.txt',sep='\s+',header=None)
data4 = pd.read_csv('Concrete_steel_cobalt.txt',sep='\s+',header=None)
data5 = pd.read_csv('Concrete_steel_strontium.txt',sep='\s+',header=None)
data6 = pd.read_csv('Concrete_steel_caesium.txt',sep='\s+',header=None)
data7 = pd.read_csv('Concrete_steel_uranium.txt',sep='\s+',header=None)
data8 = pd.read_csv('Concrete_steel_plutonium.txt',sep='\s+',header=None)
from scipy.optimize import curve_fit
import sympy as sym
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.figure(figsize=(12,12), dpi=100)
mpl.rcParams['text.usetex'] = True
mpl.rcParams['axes.linewidth'] = 1.5
plt.rc("font", size=25, family="Arial", weight='bold')
bins=np.arange(0, 450.01, 1)
x3 = data3[2] 
x4 = data4[2]
x5 = data5[2]
x6 = data6[2]
x7 = data7[2]
x8 = data8[2]
plt.hist(x3, bins=bins, histtype='step', color='Yellow',label=r'\bf Waste barrel',linewidth=1.5)
plt.hist(x4, bins=bins, histtype='step', color='MediumBlue', label=r'\bf Waste barrel+cobalt',linewidth=1.5)
plt.hist(x5, bins=bins, histtype='step', color='Orange', label=r'\bf Waste barrel+strontium',linewidth=1.5)
plt.hist(x6, bins=bins, histtype='step', color='Purple', label=r'\bf Waste barrel+caesium',linewidth=1.5)
plt.hist(x7, bins=bins, histtype='step', color='Pink', label=r'\bf Waste barrel+uranium',linewidth=1.5)
plt.hist(x8, bins=bins, histtype='step', color='Lime', label=r'\bf Waste barrel+plutonium',linewidth=1.5)
# Ticks
plt.minorticks_on()
plt.tick_params(axis='both', which='major', length=15, width=2,labelsize=22)
plt.tick_params(axis='both', which='minor', length=7.5, width=1.5,labelsize=22)
plt.xticks(np.arange(0, 550.01, step=50))
plt.yticks(np.arange(0, 10001, step=2500))
plt.yscale('log')
#Axes limits
plt.xlim(0.0, 450.01)
plt.ylim(10.0, 10001)
#Axes title
#plt.title(r'$\rm (a)$ $\rm 80\mbox{-}bin~D\mbox{$\neg$}CRY$', y=1.025)
#Axes labels
plt.xlabel(r"\bf Scattering angle [mrad]", fontsize=27)
plt.ylabel(r"\bf Counts", fontsize=27)
#No legend frame and shadow
#plt.title(r'$\rm 80\mbox{-}bin~D\mbox{$\neg$}CRY$', y=0.925, x=0.25)
handle3 = mpl.lines.Line2D([], [], c='Yellow')
handle4 = mpl.lines.Line2D([], [], c='MediumBlue')
handle5 = mpl.lines.Line2D([], [], c='Orange')
handle6 = mpl.lines.Line2D([], [], c='Purple')
handle7 = mpl.lines.Line2D([], [], c='Pink')
handle8 = mpl.lines.Line2D([], [], c='Lime')
labels=[r'\bf Waste barrel', r'\bf Waste barrel+cobalt', r'\bf Waste barrel+strontium', r'\bf Waste barrel+caesium',r'\bf Waste barrel+uranium',r'\bf Waste barrel+plutonium']
plt.legend(handles=[handle3, handle4,handle5, handle6, handle7, handle8],labels=labels,frameon=False,shadow=False)
plt.savefig("angle_counter.pdf", bbox_inches='tight')
plt.show()
