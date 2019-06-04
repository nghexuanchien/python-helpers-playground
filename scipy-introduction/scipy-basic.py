#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 21:47:44 2019

@author: chiennghe.info
"""

from scipy.stats import norm, multivariate_normal as mvn
import numpy as np
import matplotlib.pyplot as plt

norm.pdf(0)

norm.pdf(0, loc=3, scale=11) # mean, std

A = np.random.randn(10) # mean:0 , std: 1

norm.pdf(A)
norm.logpdf(A)

norm.cdf(A)
norm.logcdf(A)

B = 10 * np.random.randn(1000) + 5 # mean: 5, std: 10

C = np.random.randn(1000, 2)

plt.scatter(C[:,0], C[:,1])
plt.axis('equal')

cov = np.array([[1, 0.8], [0.8, 3]])
mean = np.array([0, 2])

D = mvn.rvs(mean=mean, cov=cov, size=1000)
plt.scatter(D[:,0], D[:,1])
plt.axis('equal')

E = np.random.multivariate_normal(mean=mean, cov=cov, size=1000)
plt.scatter(E[:,0], E[:,1])
plt.axis('equal')


F = np.linspace(0, 100, 10000)
G = np.sin(F) + np.sin(3*F) + np.sin(5*F)
plt.plot(G)

H = np.fft.fft(G)
plt.plot(H)
plt.plot(np.abs(H))