#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 12:25:26 2017

@author: claudio
"""

import numpy as np
import matplotlib.pyplot as plt

def naca_profiles(naca_string, n_points, symm=False, chord = 1.0, filename=None, plot=False):
    if len(naca_string) < 4 or len(naca_string) > 5:
        print('string not recognized')
        return
    
    if chord != 1.0:
        print("WARNING: only normalized airfoils")
    
    try:
        naca_num = int(naca_string)
    except ValueError:
        print('Profile must be 4 or 5 digits')
        return
    
    half_points = (n_points//2)*2 + 1
    
    xloc = (1 + np.cos(np.linspace(0,np.pi,num=half_points,endpoint=True)))/2
    
    ylm = np.zeros_like(xloc)
    theta = np.zeros_like(xloc)

    if len(naca_string) == 4:
        print('NACA 4 digits')
        
        P = float(naca_string[1])/10
        M = float(naca_string[0])/100
        
        print(P)
        print(M)
        
        
        if (P != 0) and (M != 0.0):
            if symm:
                ylm = 4*M* xloc*(1-xloc)
                theta = np.arctan( 4*M*(1-2*xloc) )     
            else:
                ylm[xloc <= P] = M/P**2 * xloc[xloc <= P] * (2*P - xloc[xloc <= P])
                ylm[xloc > P] = M/(1-P)**2 * (1 - 2*P + 2*P*xloc[xloc > P] - xloc[xloc > P]**2)
                
                theta[xloc <= P] = np.arctan( 2*M/P**2 * (P - xloc[xloc <= P] ) )
                theta[xloc > P]  = np.arctan( 2*M/(1-P)**2 * (P - xloc[xloc > P] ) )
        
    else:
        print('NACA 5 digits')
        
        fdig_avail = ['210', '220', '230', '240', '250']
        fdig_k = [361.4, 51.64, 15.957, 6.643, 3.23]
        fdig_q = [0.058, 0.126, 0.2025, 0.29, 0.391]
        
        try:
            idx = fdig_avail.index(naca_string[:3])
        except ValueError:
            print('5 digit NACA code not known, pleas use 210, 220, 230, 240, 250 as first 3 digits')
            return
        
        print(idx)
        k = fdig_k[idx]
        q = fdig_q[idx]
        
        if symm:
            print('WARNING: symmetric camber airfoil valid only for NACA 4 digits')
            return
        
        ylm[xloc <= q] = k/6 * (xloc[xloc <=q ]**3 - 3*q*xloc[xloc <= q]**2 +q**2*(3-q)*xloc[xloc <= q] )
        ylm[xloc >  q] = k/6*q**3 * (1-xloc[xloc > q])
        
        theta[xloc <= q] = np.arctan( k/6 * (3*xloc[xloc <= q]**2 - 6*q*xloc[xloc <= q] +q**2*(3-q)) )
        theta[xloc >  q] = np.arctan(-k/6*q**3 )
        

    
    S = int(naca_string[-2:])/100;
    thick = 5*S * (0.2969*np.sqrt(xloc) - 0.126*xloc - 0.3516*xloc**2 + 0.2843*xloc**3 -0.10150*xloc**4)
    
    xu = xloc - thick*np.sin(theta)
    yu = ylm  + thick*np.cos(theta)
    xd = xloc[-2::-1] + thick[-2::-1]*np.sin(theta[-2::-1])
    yd = ylm[-2::-1]  - thick[-2::-1]*np.cos(theta[-2::-1])
    
    xtot = np.append(xu, xd)
    ytot = np.append(yu, yd)
    
    if filename is None:
        if symm:
            filename = 'SYMM_'+naca_string+'.dat'
        else:
            filename = 'NACA_'+naca_string+'.dat'
    
    with open(filename,'w') as outfile:
        if symm:
            outfile.write('{0} {1}\n'.format('SYMM',naca_string))
        else:
            outfile.write('{0} {1}\n'.format('NACA',naca_string))
        for i in range(len(xtot)):
            outfile.write('{0:.6f}\t{1:.6f}\n'.format(xtot[i],ytot[i]))
            
    if(plot == True):
        plt.figure()
        plt.plot(xloc,ylm,'k-.',label='mean line')
        plt.plot(xloc,thick,'r-.',label='thickness')
        plt.plot(xloc,theta,'g--',label=r'$\theta$')
        plt.plot(xtot,ytot,label='profile')
        plt.axis('equal')
        plt.legend()
        if symm:
            plt.title('SYMM '+naca_string)
        else:
            plt.title('NACA '+naca_string)
    
    return        




if __name__ == "__main__":
    print("Tests")
    
    #test_str = ['123456','123','a123','1a234','1234','23100','21012']
    
    #for tmp_str in test_str:
    #    naca_profiles(tmp_str,100)
    
    naca_profiles('0006',100,plot=True,symm=False)
    naca_profiles('0012',100,plot=False,symm=False)
    naca_profiles('0016',100,plot=False,symm=False)
    naca_profiles('2412',100,plot=False,symm=False)
    naca_profiles('1412',100,plot=False,symm=False)
    naca_profiles('2212',100,plot=False,symm=False)
    naca_profiles('23012',100,plot=False,symm=False)
    
    naca_profiles('1406',100,plot=True,symm=True)
    naca_profiles('1412',100,plot=True,symm=True)
    naca_profiles('2406',100,plot=True,symm=True)
    naca_profiles('2412',100,plot=True,symm=True)