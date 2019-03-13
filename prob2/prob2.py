#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 04:34:29 2019

@author: fanwu
"""

### question 2

import numpy as np
import math

def myround(x, digit):
    if abs(x) == 0:
        return 0
    d = np.log10(float(abs(x)))
    d = int(np.floor(d)) 
    x = round(x, digit-d-1)
    return x


def mul_rd(a, n, digit):
    x = 1
    if n == 0:
        return x
    for i in range(n):
        x *= a
        x = myround(x, 5)
#        print(x)
    return x

n = 24  ## largest x^n

x = np.zeros(n+1)
for i in range(n+1):
    x[i] = mul_rd(55, i, 5) / 10**i 
    x[i] = myround(x[i] / math.factorial(i), 5)    

s_l = np.zeros(n+1)
s_r = np.zeros(n+1)

for i in range(n+1):
    if i==0:
        s_l[i] = x[i]
        s_r[i] = x[-i-1]
    else:
        s_l[i] = s_l[i-1]+x[i]
        s_r[i] = s_r[i-1]+x[-i-1]        
    s_l[i] = myround(s_l[i],5)
    s_r[i] = myround(s_r[i],5) 

s = np.exp(5.5)

x1 = np.zeros(n+1)
for i in range(n+1):
    x1[i] = mul_rd(-55, i, 5) / 10**i 
    x1[i] = myround(x1[i] / math.factorial(i), 5)    


s1_l = np.zeros(n+1)
s1_r = np.zeros(n+1)
s1_3 = 0
s1_3p = 0
s1_3n = 0
s1_4 = 0
s1_4p = 0
s1_4n = 0

seq = range(n)
even_seq = seq[::2]
odd_seq = seq[1::2]

for i in even_seq:
    s1_3p += x1[i]
    s1_3p = myround(s1_3p,5)
    
for i in odd_seq:
    s1_3n += x1[i]
    s1_3n = myround(s1_3n,5)

s1_3 = myround(s1_3p + s1_3n, 5)

for i in reversed(even_seq):
    s1_4p += x1[i]
    s1_4p = myround(s1_4p,5)
    
for i in reversed(odd_seq):
    s1_4n += x1[i]
    s1_4n = myround(s1_4n,5)

s1_4 = myround(s1_4p + s1_4n, 5)



for i in range(n+1):
    if i==0:
        s1_l[i] = x1[i]
        s1_r[i] = x1[-i-1]
    else:
        s1_l[i] = s1_l[i-1]+x1[i]
        s1_r[i] = s1_r[i-1]+x1[-i-1]        
    s1_l[i] = myround(s1_l[i],5)
    s1_r[i] = myround(s1_r[i],5) 

s1 = np.exp(-5.5)

s1_b = 1 / s_r[-1]