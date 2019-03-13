import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import newton



def df(poly):
    coef0= poly.coef
    deg = len(coef0)-1
    coef = np.zeros(deg)
    for i in range(deg):
        coef[i] = (deg-i)*coef0[i]
    s = np.poly1d(coef)
    return s

def mynewton(x0,df,f):
    return x0 - f(x0)/df(x0)

def myroot(x0,df,f):
    k = 0
    x1 = mynewton(x0,df,f)

    while (np.abs(x1-x0)>1e-6):
        k = k+1
        x0 = x1-0
        x1 = mynewton(x0,df,f)

    return x1


def cond(coef, x, df): ##a0 + a1*x + ...
    condf = 0
    for i in range(len(coef)-1):
        condf += np.abs(coef[i]*(x**(i-1))/df(x))
    return condf




k = np.array([

    2432902008176640000,

    -8752948036761600000,

    13803759753640704000,

    -12870931245150988800,

    8037811822645051776,

    -3599979517947607200,

    1206647803780373360,

    -311333643161390640,

    63030812099294896,

    -10142299865511450,

    1307535010540395,

    -135585182899530,

    11310276995381,

    -756111184500,

    40171771630,

    -1672280820,

    53327946,

    -1256850,

    20615,

    -210.0-2**(-23),

    1

]).astype(float)
    
p = np.poly1d(k[::-1])

root = 17.3

dp = df(p)
print(newton(p,root,maxiter=500))
print(myroot(root,dp,p))


delta = 0
k[-1] += delta
p = np.poly1d(k[::-1])


p = np.poly1d(k[::-1])


dp = df(p)
print(newton(p,root,maxiter=500))
print(myroot(root,dp,p))

print('%e' % cond(k, 20, dp))
