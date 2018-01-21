#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 13:19:31 2017

@author: claudio
"""

import numpy as np

def inv_t(x,c):
    theta = np.arccos(1-2*x/c)
    if theta > np.pi:
        theta -= np.pi
    return theta

def γ(θ, A, Uinf):
    g = 0
    for n in range(len(A)):
        if n == 0:
            g += A[n]*(1+np.cos(θ))/np.sin(θ)
        else:
            g += A[n]*np.sin(n*θ)
    
    return -2*Uinf*g


def du(ξ,x,y,An,Uinf,c):
    θ = inv_t(ξ,c)
    return -1/(2*np.pi)*γ(θ, An, Uinf)*y/((x-ξ)**2+y**2)


def dv(ξ,x,y,An,Uinf,c):
    θ = inv_t(ξ,c)
    return 1/(2*np.pi)*γ(θ, An, Uinf)*(x-ξ)/((x-ξ)**2+y**2)

# A_i per arco parabolico

def parabolic(tau,c,alpha):
    return np.array([alpha,4*tau/c])
    
    
# A_i per flat con flap e slat

def flap_slat(x_le, x_te, eta1, eta2, c, n, alpha):
    theta1 = inv_t(x_le,c)
    theta2 = inv_t(x_te,c)
    
    if n == 0:
        return alpha-1/np.pi*(theta1*eta1 +(np.pi-theta2)*eta2)
    else:
        A = np.zeros(n+1)
        for ii in range(n+1):
            if ii == 0:
                A[ii] = alpha -1/np.pi*(theta1*eta1 +(np.pi-theta2)*eta2)
            else:
                tmp_A = 2/(ii*np.pi)*(eta1*np.sin(ii*theta1)-eta2*np.sin(ii*theta2))
                if abs(tmp_A) < 1e-7:
                    A[ii] = 0.0
                else:
                    A[ii] = tmp_A
        return A 
    

# A_i per NACA 4
        
def naca_4(m,p,c,n,alpha):
    
    th1 = inv_t(p*c,c)



    
    A0 = alpha - m*(-5*np.pi*p**2*(2*p - 1) + p**2*(10*p*th1 + np.sqrt(-(-p + 5)**2 + 25) - 5*th1 + (p**2 - 1)*(10*p*th1 + np.sqrt(-(-p + 5)**2 + 25) - 5*th1))/(5*np.pi*p**2*(p**2 - 1)))
    
    if n == 0:
        return A0
    else:
        A = np.zeros(n+1)
        for ii in range(n+1):
            if ii == 0:
                A[ii] = A0
            elif ii == 1:
                A[ii] = m*(2*p**2*(19*p*np.sqrt(p*(-p + 10)) - 5*np.sqrt(p*(-p + 10)) + 25*th1) - 25*np.pi*p**2 - 19*p*np.sqrt(p*(-p + 10)) + 5*np.sqrt(p*(-p + 10)) - 25*th1)/(25*np.pi*p**2*(p**2 - 1))
            else:
                tmp_A = (4*m*(9*ii*p**3*np.sin(ii*th1)/5 - 9*ii*p*np.sin(ii*th1)/10 - p**2*np.sqrt(p*(-p + 10))*np.cos(ii*th1)/5 + \
                              np.sqrt(p*(-p + 10))*np.cos(ii*th1)/10 - 2*p**3*np.sin(ii*th1)/ii + p**2*np.sin(ii*th1)/ii + \
                              p*np.sin(ii*th1)/ii - np.sin(ii*th1)/(2*ii))/(np.pi*p**2*(ii**2 - 1)*(p**2 - 1)))
                if abs(tmp_A) < 1e-7:
                    A[ii] = 0.0  

                else:
                    A[ii] = tmp_A
        return A 
    
    

def naca210xx(c,n):
    r = 0.05800
    k_1 = 361.400
    
    
    if n == 0:
        return - k_1*(0.00099303790434629446*c**2 - 0.056876581270864035*c*r - np.pi*r**3 + 1.4593372759072591*r**2)/(6*np.pi)
    elif n == 1:
        return (k_1*(n*(0.000910600656021388*c**2 - 0.0529044296534789*c*r - 0.467486898212132*r**3 + 1.4024606946364*r**2) + r**3*np.sin(0.486445758635753*n))/(3*np.pi*n))
    elif n == 2:
        return (k_1*(n*(0.000678182369131891*c**2 - 0.0416474727879224*c*r - 0.413258418019524*r**3 + 1.23977525405857*r**2) + r**3*np.sin(0.486445758635753*n))/(3*np.pi*n))
    else:
        return (k_1*(0.010092*c**2*n**4*np.sin(0.486445758635753*n) + 0.0813427202889109*c**2*n**3*np.cos(0.486445758635753*n) - \
                          0.532092*c**2*n**2*np.sin(0.486445758635753*n) - 2.1850337622435*c**2*n*np.cos(0.486445758635753*n) + \
                          4.5*c**2*np.sin(0.486445758635753*n) - 0.348*c*n**4*r*np.sin(0.486445758635753*n) - 1.4024606946364*c*n**3*r*np.cos(0.486445758635753*n) + \
                          4.392*c*n**2*r*np.sin(0.486445758635753*n) + 5.60984277854558*c*n*r*np.cos(0.486445758635753*n) - 12.0*c*r*np.sin(0.486445758635753*n) + \
                          3.0*n**4*r**2*np.sin(0.486445758635753*n) - 15.0*n**2*r**2*np.sin(0.486445758635753*n) + 12.0*r**2*np.sin(0.486445758635753*n))/(3*np.pi*n*(n**4 - 5*n**2 + 4)))
        




