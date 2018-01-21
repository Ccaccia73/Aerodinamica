#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 16:33:40 2017

@author: claudio
"""

import subprocess, time, sys

print('starting')

proc = subprocess.Popen([sys.executable, 'testcr.py'],
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE  )

print('process created')

while True:
    #next_line = proc.communicate()[0]
    next_line = proc.stdout.readline()
    if next_line == '' and proc.poll() != None:
        break
    sys.stdout.write(next_line)
    sys.stdout.flush()

print('done')