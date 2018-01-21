#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 14:42:58 2017

@author: claudio
"""

import numpy as np

theta0 = np.deg2rad(45.)

x0 = 5.
y0 = 5.

xp = 6.
yp = 6.

def Tmat(x0,y0,theta):
    Trot = np.array([[np.cos(theta), np.sin(theta), 0.],[-np.sin(theta), np.cos(theta), 0.],[0., 0., 1.]])
    Ttrasl = np.array([[1., 0., -x0],[0., 1, -y0],[0., 0., 1.]])
    return np.dot(Trot,Ttrasl)

T = Tmat(x0,y0,theta0)

print(T)

x_abs = np.array([xp,yp,1])

x_rel = np.dot(T, x_abs)

print(x_rel)


class Panel():
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        
        self.x0 = (self.x1 + self.x2)/2
        self.y0 = (self.y1 + self.y2)/2
        self.theta = np.arctan2(self.y2-self.y1,self.x2-self.x1)
        
        self.b_2 = np.sqrt((x2-x1)**2 + (y2-y1)**2)/2
        
        self.Trot = np.array([[np.cos(self.theta), np.sin(self.theta), 0.],[-np.sin(self.theta), np.cos(self.theta), 0.],[0., 0., 1.]])
        self.Ttrasl = np.array([[1., 0., -self.x0],[0., 1, -self.y0],[0., 0., 1.]])
        self.Tmat = np.dot(self.Trot,self.Ttrasl)
    
    def vel(self,xp,yp,source=True):
        rel_p = np.dot(self.Tmat,np.array([xp, yp, 1.]))
        xp = rel_p[0]/rel_p[2]
        yp = rel_p[1]/rel_p[2]
        
        u = 1/(4*np.pi)*np.log(( (xp+self.b_2)**2 + yp**2 )/( (xp-self.b_2)**2 + yp**2 ) )
        v = 1/(2*np.pi)*( np.arctan( (xp+self.b_2)/yp ) - np.arctan( (xp-self.b_2)/yp ) )
        
        if source:
            #print("antitrasformare!!")
            return np.dot(self.Trot.T,np.array([u,v,1]))
        else:
            return np.dot(self.Trot.T,np.array([-v,u,1]))
        