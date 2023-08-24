# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 17:56:54 2023

@author: victo
"""
import numpy as np
T=float(input('Time period of satellite in sec ='))
G=6.67*1e-11
R=6371
M=5.972*1e24
def r(T):
    return ((G*(M)*(T**2))/(4*np.pi**2))**(1/3)*1e-3 -R
print('height from surface = %d km'%r(T))
h= r(24*3600)-r(23.56*3600)
print('difference between height of satellite for 24h orbit and sideral day orbit is = %d km'%h)