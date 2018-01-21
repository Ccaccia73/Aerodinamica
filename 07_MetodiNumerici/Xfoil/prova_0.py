#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:47:32 2017

@author: claudio
"""

import numpy as np
import matplotlib.pyplot as plt

import xfoil_module as xf

print xf.find_coefficients('naca0012',0.0,NACA=True)

#upper = {'x':[0,.1,10,20,30], 'y':[0,2,4,2,1]}
#lower = {'x':[0,.1,10,20,30], 'y':[0,-10,-2,-1,0]}
#plt.plot(lower['x'], lower['y'], 'r')
#plt.plot(upper['x'], upper['y'], 'r', label = 'original data')
#rotated_upper, rotated_lower = xf.prepare_xfoil(upper, lower, 1.0, reposition=True)
#print rotated_upper
#print rotated_lower
#
#plt.plot(rotated_lower['x'], rotated_lower['y'], 'b')
#plt.plot(rotated_upper['x'], rotated_upper['y'], 'b', label='after LE rotation/translation')
#plt.legend(loc='best')
#plt.xlabel('x-coordinate')
#plt.ylabel('y-coordinate')
#plt.grid()
#plt.show()
