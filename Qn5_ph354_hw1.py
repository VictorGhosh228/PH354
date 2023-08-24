# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 11:09:26 2023

@author: victo
"""

import numpy as np
E= float(input('energy of particle in eV is = '))
V=float(input('Barrier potential in eV is = '))
k=np.sqrt(1-(V/E))
R=((1-k)**2)/(1+k)**2
T=4*k/((1+k)**2)
print ('Reflection probability is %.2f'%R)
print ('Transmission probability is %.2f'%T)