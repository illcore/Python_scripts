import pandas as pd
import sympy as sym
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.figure(figsize=(12,12), dpi=100)
mpl.rcParams['text.usetex'] = True
mpl.rcParams['axes.linewidth'] = 1.5
plt.rc("font", size=25, family="Arial", weight='bold')
rect1=plt.Rectangle(xy=(0,0), width=10, height=10, color="Green") #Starts at left corner (left edge) of the rectangle
rect2=plt.Rectangle(xy=(4,4), width=2, height=2, color="Red")
disc1=plt.Circle((4,4), 1, color="Blue")
circle1 = plt.Circle((8,2), 1, color="Yellow", fill=False)
plt.plot((0,2),(0,2), color="Orange") #(x1,x2),(y1,y2)
plt.annotate("", xytext = (7.25,7.5), xy = (9,7.5), ha = 'center', va = 'bottom', arrowprops=dict(arrowstyle="->"), color='Black')
plt.annotate("", xytext = (7.5,7.25), xy = (7.5,9), ha = 'center', va = 'bottom', arrowprops=dict(arrowstyle="->"), color='Black')
plt.text(9, 7.4, r"\bf x")
plt.text(7.40, 9.1, r"\bf y")
fig=plt.gcf()
ax=fig.gca()
ax.add_patch(rect1)
ax.add_patch(rect2)
ax.add_patch(disc1)
ax.add_patch(circle1)
plt.minorticks_on()
plt.tick_params(axis='both', which='major', length=15, width=2,labelsize=22)
plt.tick_params(axis='both', which='minor', length=7.5, width=1.5,labelsize=22)
plt.xticks(np.arange(0, 10.0001, step=1))
plt.yticks(np.arange(0, 10.0001, step=1))
#Axes limits
plt.xlim(0.0, 10.0001)
plt.ylim(0.0, 10.0001)
plt.xlabel(r"\bf Horizontal distance [cm]", fontsize=27)
plt.ylabel(r"\bf Vertical distance [cm]", fontsize=27)
#No legend frame and shadow
handle3 = mpl.lines.Line2D([], [], c='Green', lw=20)
handle4 = mpl.lines.Line2D([], [], c='Red',lw=20)
handle5 = mpl.lines.Line2D([], [], c='Blue', lw=20)
handle6 = mpl.lines.Line2D([], [], c='Yellow', lw=20)
handle7 = mpl.lines.Line2D([], [], c='Orange', lw=20)
labels=[r'\bf Background - Rectangle', r'\bf Square', r'\bf Disc', r'\bf Circle', r'\bf Line']
plt.legend(handles=[handle3, handle4, handle5, handle6, handle7], labels=labels, loc="upper left", bbox_to_anchor=(1, 0.65), frameon=False, shadow=False)
plt.savefig("Drawing.pdf", bbox_inches='tight')
plt.show()

