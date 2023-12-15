import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


y = []

t = np.arange(0,100,1) # range from 0 to 100 in steps of 1

x = np.sin(np.pi * t)


plt.style.use('_mpl-gallery')

fig, tx = plt.subplots()

tx.plot(t,x,linewidth=2.0)
plt.show()