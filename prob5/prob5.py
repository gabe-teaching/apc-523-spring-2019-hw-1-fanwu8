import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import newton

    
### question 5
def get_e(n):
   s = np.power(10, n)
   return(np.power(1+1/s, s))
       

n = 50    

e_s = np.zeros(n)
for i in range(n):
   e_s[i] = get_e(i)
   if i>1:
       if abs(e_s[i]-e_s[i-1])<10**(-12):
           ind = i
           break

for i in range(ind+1):
   print('%.13g' %e_s[i])
