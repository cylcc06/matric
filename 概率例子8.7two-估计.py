import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,1,100)

plt.plot(x,(1-x)/np.abs(np.log(x)), 'go--',label='E[sita|X=x]')
plt.plot(x,x,'r--',label='f(sita|X)')
plt.legend()
plt.show()