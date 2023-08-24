# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 10:22:27 2023

@author: victo
"""

import numpy as np
x= float(input('distance to the planet in light years ='))
v=float(input('velocity of spaceship in terms of speed of light = '))
t_earth=(x)/v
t_pass=t_earth*(np.sqrt(1-v**2))
print('(a)-----------------------------------------------------------')
print('time according to an observer in rest frame earth is %.3f yr'%t_earth)
print('(b)-----------------------------------------------------------')
print('time according to an passenger is %.3f yr'%t_pass)
print('-----------*-----------------------*-----------------*-----------')