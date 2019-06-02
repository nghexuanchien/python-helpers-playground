#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 23:12:37 2019

@author: chiennghe.info
"""

import matplotlib.pyplot as plt
import pandas as pd

A = pd.read_csv('homes.csv').as_matrix() # Home sale statistics. Fifty home sales, with selling price, asking price, living space, rooms, bedrooms, bathrooms, age, acreage, taxes. There is also an initial header line.
selling_prices = A[:,0]
living_spaces = A[:,2]

plt.scatter(living_spaces, selling_prices);
plt.xlabel('Living Space')
plt.ylabel('Selling Price')
plt.title('Want to buy a house?')

