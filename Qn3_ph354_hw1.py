# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 19:56:13 2023

@author: victo
"""

import numpy as np
x=float(input('x coordinate of point is ='))
y=float(input('y coordinate of point is = '))
r=np.sqrt(x**2+y**2)
if (x>0 and y>0):
    Theta=np.arctan(y/x)*(180/np.pi)
elif (x<0 and y>0):
    Theta=(np.pi+np.arctan(y/x))*(180/np.pi)
elif (x<0 and y<0):
    Theta= (-np.pi+np.arctan(y/x))*(180/np.pi)
elif (x>0 and y<0):
    Theta=np.arctan(y/x)*(180/np.pi)
elif (x==0 and y>0):
    Theta=90
elif (x==0 and y<0):
    Theta=-90
elif (x>0 and y==0):
    Theta=0
elif (x<0 and y==0):
    Theta=180
else:
    Theta=0

print('polar coordinate corresponding to given cartesian is ( %.2f ,%.1f deg )'%(r,Theta))