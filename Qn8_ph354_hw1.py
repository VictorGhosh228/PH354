# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 15:57:55 2023

@author: victo
"""

import numpy as np
#def f(i,j,k):
 #   return 1/(np.sqrt(i**2+j**2+k**2))
M=0.0
L=50
for i in range(-L,L+1):
    for j in range (-L,L+1):
        for k in range (-L,L+1):
            if i==0 and j==0 and k==0:
                continue
            else:
               M+=(-1)**(i+j+k)/(np.sqrt(i**2+j**2+k**2))
               print(M,i,j,k,(i**2+j**2+k**2))
print(M)