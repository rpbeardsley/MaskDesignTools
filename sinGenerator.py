from sys import argv
import math
import numpy as np
import matplotlib.pyplot as plt

width = 2.5
x0 = 50
x1 = 100
y0 = 20
y1 = 100
Res = 800
L = 2*(x1-x0)

x = np.linspace(x0,x1,Res)
y = ((y0-y1)/2)*np.cos(2*math.pi*((x-x0)/L)) + ((y0+y1)/2)

plt.figure(1)
plt.plot(x,y,'b-')

f = open('PATH_HERE.tco', 'w')
f.write("width " + str(width) + "\n")
f.write('path -! ')
for C in range (0, x.size):    
    f.write(str(round(x[C],3)))
    f.write(' ')
    f.write(str(round(y[C],3)))
    f.write(' ')

f.close()

#f = open('cosTestPoly.tco', 'w')

#f.write('polygon -! ')
#f.write(str(x0) + " " + str(y0) + " ")

#for C in range (0, x.size):
#    f.write(str(round(x[C],3)))
#    f.write(' ')
#    f.write(str(round(y[C],3) + (width/2)))
#    f.write(' ')

#f.write(str(x1) + " " + str(y1) + " ")

#for C2 in range (0, x.size):
#    f.write(str(round(x[x.size-1-C2],3)))
#    f.write(' ')
#    f.write(str(round(y[x.size-1-C2],3) - (width/2)))
#    f.write(' ')

#f.close()
