#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 00:02:11 2019

@author: fanwu
"""
import numpy as np
from scipy import integrate

def back(yn1, n):
    yn = (np.e - yn1) / (n+1)
    return  yn

def func(x):
    return x**20*np.exp(x)

yn = 0
for i in range(31,19,-1):
    yn = back(yn, i)
    print(yn)

S,err=integrate.quad(func,0,1)
print(S)