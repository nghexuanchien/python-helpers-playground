#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 23:12:37 2019

@author: chiennghe.info
"""

import matplotlib.pyplot as plt
import numpy as np

A = np.linspace(0, 10, 30)
B = np.sin(A)
plt.plot(A, B)
plt.xlabel('A series')
plt.ylabel('B series')
plt.title('Sin function')
plt.show()

