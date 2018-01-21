#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 11:07:55 2017

@author: claudio
"""

import numpy as np
import matplotlib.pyplot as plt

def joukowsky_transform(z,c):
    return z + c**2/z



def KT_transform(z,alpha):
    n = 2 - alpha/np.pi
    return n*( ( 1 + 1/z )**n + ( 1 - 1/z )**n )/( ( 1 + 1/z )**n - ( 1 - 1/z )**n )


def Gamma(U,R,alpha,beta):
    return -4*np.pi*R*U*np.sin(alpha-beta)


def cylinder_potential(zeta,zeta0,Uinf,G,R,alpha):
    
    F = np.zeros_like(zeta)
    
    n_xi, n_eta = zeta.shape
    for ii in range(n_xi):
        for jj in range(n_eta):
            if abs(zeta[ii,jj]-zeta0) <= R:
                F[ii,jj] = np.nan
            else:
                F[ii,jj] = Uinf*np.exp(-1j*alpha)*zeta[ii,jj] - 1j*G/(2*np.pi)*np.log(zeta[ii,jj]-zeta0) + Uinf*R**2*np.exp(1j*alpha)/(zeta[ii,jj]-zeta0)
                                        
    return F


def cylinder_velocity(zeta,zeta0,Uinf,G,R,alpha):
    
    w = np.zeros_like(zeta)
    
    n_xi, n_eta = zeta.shape
    for ii in range(n_xi):
        for jj in range(n_eta):
            if abs(zeta[ii,jj]-zeta0) <= R:
                w[ii,jj] = np.nan
            else:
                w[ii,jj] = Uinf*np.exp(-1j*alpha) - \
                1j*G/(2*np.pi*(zeta[ii,jj]-zeta0))- \
                Uinf*R**2*np.exp(1j*alpha)/(zeta[ii,jj]-zeta0)**2
                                        
    return w


def airfoil_velocity(zeta,zeta0,Uinf,G,R,alpha,c0):
    
    w = np.zeros_like(zeta)
    
    n_xi, n_eta = zeta.shape
    for ii in range(n_xi):
        for jj in range(n_eta):
            if abs(zeta[ii,jj]-zeta0) <= R:
                w[ii,jj] = np.nan
            else:
                w[ii,jj] = (Uinf*np.exp(-1j*alpha) - \
                1j*G/(2*np.pi*(zeta[ii,jj]-zeta0))- \
                Uinf*R**2*np.exp(1j*alpha)/(zeta[ii,jj]-zeta0)**2)/(1-c0**2/zeta[ii,jj]**2)
                                        
    return w


def dzdzeta(zt,n):
    return 4*n**2*((zt - 1)/zt)**n*((zt + 1)/zt)**n/(zt**2*((zt - 1)/zt)**(2*n) - 2*zt**2*((zt - 1)/zt)**n*((zt + 1)/zt)**n + zt**2*((zt + 1)/zt)**(2*n) - ((zt - 1)/zt)**(2*n) + 2*((zt - 1)/zt)**n*((zt + 1)/zt)**n - ((zt + 1)/zt)**(2*n))

def airfoil_velocity_KT(zeta,zeta0,Uinf,G,R,alpha,aKT):
    
    w = np.zeros_like(zeta)
    
    n_xi, n_eta = zeta.shape
    for ii in range(n_xi):
        for jj in range(n_eta):
            zt = zeta[ii,jj]
            if abs(zt-zeta0) <= R:
                w[ii,jj] = np.nan
            else:
                n = 2-aKT/np.pi

                w[ii,jj] = (Uinf*np.exp(-1j*alpha) - \
                1j*G/(2*np.pi*(zt-zeta0))- \
                Uinf*R**2*np.exp(1j*alpha)/(zt-zeta0)**2)/dzdzeta(zt,n)
                                        
    return w


def Cp_contour(w,U0):
    return 1-(np.abs(w)/U0)**2



def compute_Cp(zeta0,Uinf,G,R,alpha,c0,beta,npoints):
    
    theta_us = np.linspace(beta+0.001,np.pi-beta,npoints)
    theta_ls = np.linspace(np.pi-beta,2*np.pi+beta-0.001,npoints)
    
    zeta_us = zeta0+R*np.exp(1j*theta_us)
    zeta_ls = zeta0+R*np.exp(1j*theta_ls)
    
    wzeta_us = Uinf*np.exp(-1j*alpha) - 1j*G/(2*np.pi*(zeta_us-zeta0))-Uinf*R**2*np.exp(1j*alpha)/(zeta_us-zeta0)**2
    wzeta_ls = Uinf*np.exp(-1j*alpha) - 1j*G/(2*np.pi*(zeta_ls-zeta0))-Uinf*R**2*np.exp(1j*alpha)/(zeta_ls-zeta0)**2
    
    Cp_cyl_us = 1-np.abs(wzeta_us)**2/Uinf**2
    Cp_cyl_ls = 1-np.abs(wzeta_ls)**2/Uinf**2
    
    wz_us = wzeta_us/(1-c0**2/zeta_us**2)
    wz_ls = wzeta_ls/(1-c0**2/zeta_ls**2)

    Cp_af_us = 1-np.abs(wz_us)**2/Uinf**2
    Cp_af_ls = 1-np.abs(wz_ls)**2/Uinf**2

    
    xi_us = zeta_us.real
    xi_ls = zeta_ls.real
    
    x_us = joukowsky_transform(zeta_us,c0).real
    x_ls = joukowsky_transform(zeta_ls,c0).real
    
    return (xi_us,Cp_cyl_us),(xi_ls,Cp_cyl_ls),(x_us,Cp_af_us),(x_ls,Cp_af_ls)


def compute_Cp_KT(zeta0,Uinf,G,R,alpha,alphaKT,beta,npoints):
    
    n = 2 - alphaKT/np.pi
        
    theta_us = np.linspace(beta+0.001,np.pi-beta,npoints)
    theta_ls = np.linspace(np.pi-beta,2*np.pi+beta-0.001,npoints)
    
    zeta_us = zeta0+R*np.exp(1j*theta_us)
    zeta_ls = zeta0+R*np.exp(1j*theta_ls)
    
    wzeta_us = Uinf*np.exp(-1j*alpha) - 1j*G/(2*np.pi*(zeta_us-zeta0))-Uinf*R**2*np.exp(1j*alpha)/(zeta_us-zeta0)**2
    wzeta_ls = Uinf*np.exp(-1j*alpha) - 1j*G/(2*np.pi*(zeta_ls-zeta0))-Uinf*R**2*np.exp(1j*alpha)/(zeta_ls-zeta0)**2
    
    Cp_cyl_us = 1-np.abs(wzeta_us)**2/Uinf**2
    Cp_cyl_ls = 1-np.abs(wzeta_ls)**2/Uinf**2
    
    wz_us = wzeta_us/dzdzeta(zeta_us,n)

    wz_ls = wzeta_ls/dzdzeta(zeta_ls,n)

    Cp_af_us = 1-np.abs(wz_us)**2/Uinf**2
    Cp_af_ls = 1-np.abs(wz_ls)**2/Uinf**2

    
    xi_us = zeta_us.real
    xi_ls = zeta_ls.real
    
    x_us = KT_transform(zeta_us,alphaKT).real
    x_ls = KT_transform(zeta_ls,alphaKT).real
    
    return (xi_us,Cp_cyl_us),(xi_ls,Cp_cyl_ls),(x_us,Cp_af_us),(x_ls,Cp_af_ls)


def plot_cyl_airfoil(z_c0,c0,delta,alphaKT=0.0,joukowski=True):
    plt.figure(figsize=(16,8))
    plt.subplot(1,2,1)
    plt.plot(z_c0.real,z_c0.imag,c=(0.4,0.4,0.4))
    plt.scatter(0,0,s=180,c=(0.0,0.0,0.0),marker='+',label='origin')
    plt.scatter(delta.real,delta.imag,s=80,c=(0.0,0.0,0.25),marker='x',label=r'cyl. center $\zeta_0$')
    plt.scatter(c0,0,s=80,c=(0.35,0.0,0.0),label=r'crit. point $c_0$')
    plt.legend(loc=1)
    plt.axis('equal')
    plt.xlabel(r'$\xi$')
    plt.ylabel(r'$\eta$')
    plt.title('cylinder')
    if joukowski:
        z0 = joukowsky_transform(z_c0,c0)
    else:
        z0 = KT_transform(z_c0,alphaKT)
    plt.subplot(1,2,2)
    plt.plot(z0.real,z0.imag)
    plt.xlabel(r'x')
    plt.ylabel(r'y')
    if joukowski:
        plt.title('Joukowski airfoil')
    else:
        plt.title('Karman Treffz airfoil')
    plt.axis('equal');
    
def plot_stream(z,F,w,z_c0,border=5,lv=25,kst=10,sc=1,nm='cylinder'):
    plt.figure(figsize=(16,8))
    plt.subplot(1,2,1)
    plt.contour(z.real,z.imag,F.imag,lv,cmap='coolwarm')
    plt.fill(z_c0.real,z_c0.imag,c=(0.0,0.0,0.27))
    plt.title(nm+r' $\Psi$ contour')
    plt.axis('equal')
    plt.axis([-border,border,-border,border]);
    plt.subplot(1,2,2)
    plt.title(nm+r' velocity field')
    plt.fill(z_c0.real,z_c0.imag,c=(0.0,0.0,0.27))
    #plt.streamplot(ζ.real, ζ.imag, wc1.real, -wc1.imag, density=2, linewidth=1, arrowsize=2, arrowstyle='->')
    cm =plt.quiver(z[::kst,::kst].real, z[::kst,::kst].imag, \
                 w[::kst,::kst].real, -w[::kst,::kst].imag,np.abs(w)[::kst,::kst],cmap='coolwarm',scale=sc)
    
    plt.colorbar(cm)
    plt.axis('equal')
    plt.axis([-border, border, -border, border]);
    
def plot_Cp_contour(zc,z_c0,Cp_c,za,z_airfoil,Cp_a,lv=25,border=5):
    plt.figure(figsize=(16,8))
    plt.subplot(1,2,1)
    plt.title('Cylinder $C_p$ contour')
    plt.xlabel(r'$\xi$')
    plt.ylabel(r'$\eta$')

    plt.contourf(zc.real,zc.imag,Cp_c,lv,cmap='coolwarm')
    plt.fill(z_c0.real,z_c0.imag,c=(0.0,0.0,0.27))
    #plt.plot(ζ_c0.real,ζ_c0.imag)
    plt.axis('equal')
    plt.subplot(1,2,2)
    cm =plt.contourf(za.real,za.imag,Cp_a,lv,cmap='coolwarm')
    plt.fill(z_airfoil.real,z_airfoil.imag,c=(0.0,0.0,0.27))
    #plt.plot(z_airfoil.real,z_airfoil.imag)
    plt.colorbar(cm)
    plt.title('Airfoil $C_p$ contour')
    plt.xlabel(r'x')
    plt.ylabel(r'y')
    plt.axis('equal')
    plt.axis([-border, border, -border, border]);
 
    
def plot_Cp_surface(cyl_up,cyl_down,af_up,af_down):
    plt.figure(figsize=(16,10))
    plt.subplot(1,2,1)
    plt.plot(cyl_up[0],cyl_up[1],label='cyl upper surf.')
    plt.plot(cyl_down[0],cyl_down[1],label='cyl lower surf.')
    plt.gca().invert_yaxis()
    plt.xlabel(r'$\xi$')
    plt.ylabel(r'$-C_p$')
    plt.legend()
    plt.axis('equal')
    plt.subplot(1,2,2)
    plt.plot(af_up[0],af_up[1],label='airfoil upper surf.')
    plt.plot(af_down[0],af_down[1],label='airfoil lower surf.')
    plt.gca().invert_yaxis()
    plt.xlabel(r'$\frac{x}{c}$')
    plt.ylabel(r'$-C_p$')
    plt.legend()
    plt.axis('equal');
