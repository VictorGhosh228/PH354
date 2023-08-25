# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 10:58:44 2023

@author: victo
"""

import numpy as np
n=int(input('n= '))
k=int(input('k= '))
def binomial(n,k):
    if k==0:
        return 1
    
    else:
        return int((np.math.factorial(n))/((np.math.factorial(n-k))*(np.math.factorial(k))))
print('PROBLEM (A)-------------------------------------------')
print('value of binomial function with n=%d and k=%d is= %d'%(n,k,binomial(n, k)))
print('------------------------------------------------------')
print('PROBLEM(B)--------------------------------------------')
print("Pascal's triangle is -")
for i in range (1,10):
    p=[]
    for j in range (0,i+1):
        p.append(binomial(i, j))
    print(*p)
print('------------------------------------------------------')
print('PROBLEM (C)-------------------------------------------')
N=100
K=60
P=binomial(N, K)/(2**100)
print('probability of having exactly 60 heads is %.2f '%P)
q=0
for j in range (60,101):
    q=q+(binomial(N, j)/2**100)
print('probability of having 60 or more heads is %.2f '%q)
print('----------------------end-----------------------------')
     
