import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb, perm
x=np.linspace(0,50,50)

p1=0.46
p2=0.52
plt.plot(x,comb(50,x)*(p1**x) * (1-p1)**(50-x), 'go--',label='sita=1')
plt.plot(x,comb(50,x)*(p2**x) * (1-p2)**(50-x),'r-')
plt.plot(x,np.abs(comb(50,x)*(p1**x) * (1-p1)**(50-x) - comb(50,x)*(p2**x) * (1-p2)**(50-x)),'b')
plt.legend()
plt.show()
print(comb(50,24)*(p1**24) * (1-p1)**(50-24))
print(comb(50,24)*(p2**24) * (1-p2)**(50-24))