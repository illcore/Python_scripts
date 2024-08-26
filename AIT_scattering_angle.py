import pandas as pd
data = pd.read_csv('U_Wall.csv',sep=',',header=None)
import sympy as sym
import numpy as np
import math
ID=np.array(data[0])
xcor=data[1]
ycor=data[2]
zcor=data[3]
Energy=data[4]
count=0
f = open("my_angles.txt", "w")
for x in range(len(ID)-3):
	if ID[x]==ID[x+3] :     
		PrintID=ID[x]
		PrintEnergy=Energy[x]
		vec1x=xcor[x+1]-xcor[x]
		vec2x=xcor[x+3]-xcor[x+2]
		vec1y=ycor[x+1]-ycor[x]
		vec2y=ycor[x+3]-ycor[x+2]
		vec1z=zcor[x+1]-zcor[x]
		vec2z=zcor[x+3]-zcor[x+2]
		quotient1=math.sqrt(vec1x**2+vec1y**2+vec1z**2)
		quotient2=math.sqrt(vec2x**2+vec2y**2+vec2z**2)
		quotient=quotient1*quotient2
		Angle=math.acos((vec1x*vec2x+vec1y*vec2y+vec1z*vec2z)/quotient)
		Angle=Angle*1000                		 
		print(PrintID, PrintEnergy, Angle)
		f.write(str(PrintID)+" "+str(PrintEnergy)+" "+str(Angle)+"\n")

f.flush()
f.close		

    
    	
   
  
    	
