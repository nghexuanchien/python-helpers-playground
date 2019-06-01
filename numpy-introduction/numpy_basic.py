# -*- coding: utf-8 -*-
"""
chiennghe.info

This is a playground for numpy basic intructions
"""

import numpy as np

A = np.array([1,2,3,4])
A1 = A + A
A2 = 2*A
A3 = A**2
A4 = np.sqrt(A) # np.log(A) np.exp(A)

B = np.array([1,2])
C = np.array([3,4]);
D = B * C
np.sum(D)
D.sum()
(B*C).sum()
np.dot(B, C)
B.dot(C)
np.inner(B, C)
np.outer(B, C)

magnitude = np.sqrt((B * B).sum())
magnitude = np.linalg.norm(B)

cos = B.dot(C) / (np.linalg.norm(B) * np.linalg.norm(C))
angle = np.arccos(cos)

E = np.array([[1,2], [3,4]])
E[0, 1]
E.T
E1 = np.linalg.inv(E)
E1.dot(E)
E.dot(E1)
np.linalg.det(E) # matrix determinant
np.diag(E)
np.diag(E).sum() # matrix trace
np.trace(E)
np.diag([1, 4])
E1 = np.array([1,2])
np.linalg.solve(E, E1) # Ex = E1



np.zeros(10)
np.ones((10, 10))
np.random.random((10, 10)) #uniform distribution
F = np.random.randn(10, 10) #gaussian distribution - mean: 0, gaussian: 1
F.mean()
F.var()