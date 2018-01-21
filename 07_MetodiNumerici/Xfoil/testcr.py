#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 16:33:33 2017

@author: claudio
"""

import time, sys
for i in range(200):
    sys.stdout.write( 'reading %i\n'%i )
    time.sleep(.02)