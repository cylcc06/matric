import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,2,100)

plt.plot(x,np.exp(-x),'go--',label='A')
plt.plot(x,np.exp(x),label='B')
plt.legend()
plt.show()