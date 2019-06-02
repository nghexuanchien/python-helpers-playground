#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 23:12:37 2019

@author: chiennghe.info
"""

import matplotlib.pyplot as plt
import pandas as pd

A = pd.read_csv('homes.csv').as_matrix()
rooms = A[:,3]
plt.hist(rooms, bins=8)
plt.xlabel('Number of rooms')
plt.ylabel('Number of houses')
plt.title('Which house segment is the most popular?')

