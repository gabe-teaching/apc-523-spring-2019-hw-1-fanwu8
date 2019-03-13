#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 01:45:13 2019

@author: fanwu
"""


import numpy as np

import matplotlib.pyplot as plt

from scipy.optimize import newton

x = np.linspace(0.0001,0.01,100)
condf_x = x / (np.exp(x) - 1) 
condA_x = np.exp(x) / x
plt.plot(x, condA_x)




# print(dw(7), dw(10), dw(10.5))

# p = np.polynomial.Polynomial(k)

# print(newton(w, 21, maxiter=500))

# # print p(2)
