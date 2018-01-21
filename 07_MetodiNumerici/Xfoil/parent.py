#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 15:42:02 2017

@author: claudio
"""

import subprocess
import sys


#def run(cmd, logfile):
#    p = subprocess.Popen(['xfoil'],
#                         stdin=subprocess.PIPE,
#                         stdout=logfile,
#                         stderr=subprocess.PIPE)
#    ret_code = p.wait()
#    logfile.flush()
#    return ret_code

logfile = open('logfile.txt','w')


foils = ['0006','0012','0016','1412','2212','2412']

for foil in foils:
    p = subprocess.Popen(['xfoil'],
                         shell=False,
                         stdin=subprocess.PIPE,
                         stdout=logfile,
                         stderr=logfile)

    s0 = "LOAD NACA_{0}.dat\n".format(foil)
    s0 += "PANE\n"
    s0 += "OPERi\n"
    s0 += "PACC\n"
    s0 += "CLi_NACA_{0}.dat\n".format(foil)
    s0 += "\n"
    s0 += "ASEQ -5 15 0.5\n"
    s0 += "P\n"
    s0 += "\n"
    s0 += "QUIT\n"
    out, err = p.communicate(s0.encode())




#foils = ['1412','2212','2412']
foils = ['1412','2212','2412','23012']

angles = ['-2','-1','0','1','2','3','4']


for foil in foils:
    p = subprocess.Popen(['xfoil'],
                         shell=False,                     
                         stdin=subprocess.PIPE,
                         stdout=logfile,
                         stderr=logfile)
    
    s0 = ""
    s0 += "LOAD NACA_{0}.dat\n".format(foil)
    s0 += "PANE\n"
    s0 += "OPERi\n"
    for angle in angles:
        s0 += "ALFA {0}\n".format(angle)
        s0 += "CPWR CPi_NACA_{0}_{1}.dat\n".format(foil,angle)
    s0 += "\n"
    s0 += "QUIT\n"
    out, err = p.communicate(s0.encode())

#print(out.decode())
#print(err.decode())



#for foil in foils:
#    p = subprocess.Popen(['xfoil'],
#                         shell=False,
#                         stdin=subprocess.PIPE,
#                         stdout=logfile,
#                         stderr=logfile)
#
#    s0 = "LOAD NACA_{0}.dat\n".format(foil)
#    s0 += "PANE\n"
#    s0 += "OPERi\n"
#    s0 += "PACC\n"
#    s0 += "CLi_NACA_{0}.dat\n".format(foil)
#    s0 += "\n"
#    s0 += "ASEQ -5 15 0.5\n"
#    s0 += "P\n"
#    s0 += "\n"
#    s0 += "QUIT\n"

foils = ['1406','1412','2406','2412']

for foil in foils:
    p = subprocess.Popen(['xfoil'],
                         shell=False,
                         stdin=subprocess.PIPE,
                         stdout=logfile,
                         stderr=logfile)

    s0 = "LOAD SYMM_{0}.dat\n".format(foil)
    s0 += "PANE\n"
    s0 += "OPERi\n"
    s0 += "PACC\n"
    s0 += "CLi_SYMM_{0}.dat\n".format(foil)
    s0 += "\n"
    s0 += "ASEQ -5 15 0.5\n"
    s0 += "P\n"
    s0 += "\n"
    s0 += "QUIT\n"
    out, err = p.communicate(s0.encode())

#p.stdin.write(s.encode())
##print("send")
#p.stdin.write(s0.encode())
#p.stdin.write(s1.encode())
#p.stdin.write(s2.encode())
#p.stdin.write(s3.encode())
#p.stdin.write(s4.encode())
#p.stdin.write(s5.encode())
#p.stdin.write(s6.encode())
#p.stdin.write(s7.encode())
#p.stdin.write(s8.encode())
#p.stdin.write(s9.encode())
#
#p.stdout.flush()
#p.kill()

logfile.close()

print("finish")


#print(out.decode())

#print(err.decode())

#p.stdin.write(s1.encode())
#print(out.decode())

#print(err.decode())


#print(out.decode())

#print(pippo.decode())
