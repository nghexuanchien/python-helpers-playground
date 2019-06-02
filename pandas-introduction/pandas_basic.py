# -*- coding: utf-8 -*-
"""
chiennghe.info

This is an illustration of pandas basic instructions
"""
import pandas as pd

A = pd.read_csv('FL_insurance_sample.csv') #header=None for csv file without header
type(A)
A.info()
A.head(10)
A.columns
A['policyID']
A.policyID
type(A['policyID'])

A[['policyID', 'statecode']]
type(A[['policyID', 'statecode']])
A['active'] = 1

A['total_tiv'] = A.apply(lambda row: row['tiv_2011'] + row['tiv_2012'], axis=1)
A[['tiv_2011', 'tiv_2012', 'total_tiv']]


A.ix[0]
A.iloc[0]
type(A.iloc[0])
A[A['point_granularity'] > 1]

B = A.as_matrix()
type(B)

C = pd.read_csv('FL_insurance_sample.csv')
D = pd.merge(A, C, on='policyID')
D = A.merge(C, on='policyID')
D.info()