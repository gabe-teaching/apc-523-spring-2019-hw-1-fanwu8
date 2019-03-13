import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import newton

a0 = np.linspace(1, 10, 1001)
a = a0
n = 51

for i in range(n):
   a = np.sqrt(a)

for i in range(n):
   a = np.power(a, 2)
   
plt.plot(a0, a)
plt.plot(a0, a0)
