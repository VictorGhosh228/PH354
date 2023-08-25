# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 14:54:26 2023

@author: victo
"""

def f(n):
    return (4*n+2)/(n+2)
c=[1]
n=0
while c[n]<1e9:
    c.append(f(n)*c[n])
    n=n+1
print('catalan numbers \n ',c)   