# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 17:44:36 2023

@author: victo
"""

import numpy as np
#from sympy import symbols, Eq, solve
A=int(input('Mass Number = '))
Z=int(input('Atomic number = '))
a1=15.67
a2=17.23
a3=0.75
a4=93.2
if A%2==0:
    if Z%2==0:
        a5=12.0
    else :
        a5=-12.0
else:
    a5=0
def B(A,Z):
    return (a1*A-a2*A**(2/3)-a3*(Z**2)/(A**(1/3)) -a4*((A-2*Z)**2)/(A) +a5/(A**(1/2)))
print('Demo------------------------------------------------------------')
print('PROBLEM (A)')
print('Binding Energy of atom with %d A and %d Z is %d MeV'%(58,28,B(58,28)))
print('-----------------------------------------------------------------')
print('Binding energy of atom with atomic number %d and Mass number %d is %d Mev'%(Z,A,B(A, Z)))
B_A=B(A, Z)/A
print('-----------------------------------------------------------------')
print('PROBLEM (B)')
print('Binding energy per nucleon is %d MeV'%B_A)
print('-----------------------------------------------------------------')
print('PROBLEM (C)')
B1=[]
for i in range (Z,(3*Z)+1):
    B1.append(B(i, Z)/i)
    #print('Binding energy per nucleon for mass number %d and atomic number %d is %d MeV'%(i,Z,B1))
    
#print(B1)
B_max=np.max(B1)
A_s=B1.index(B_max)+Z
print('for atomic number %d maximum Binding energy per nucleon is %.4f MeV i.e most stable nucleus is with mass number %d'%(Z,B_max,A_s))
print('------------------------------------------------------------------')
print('PROBLEM (D)')
S_A=[]
for j in range(1,101):
    Bj=[]
    for i in range(j,(3*j)+1):
        Bj.append(B(i,j)/i)
    #print(Bj)
    Bj_max=np.max(Bj)
    Aj_s=Bj.index(Bj_max)+j
    S_A.append((j,Aj_s))
    #print(j,Aj_s)
print('Most stable atoms are -',S_A) 
print('--------------------------------------------------------------------')  
 
