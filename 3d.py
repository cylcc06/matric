# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
# import matplotlib.pyplot as plt
# #生成画布
# figure=plt.figure()
# ax=figure.add_subplot(111,projection='3d')
# #生成向量
# z=np.linspace(0,6,1000)
# r=1
# x=r*np.sin(np.pi*2*z)
# y=r*np.cos(np.pi*2*z)
# ax.plot(x,y,z)
# plt.show()

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
ax=Axes3D(fig)
X=np.arange(-4,4,0.01)
Y=np.arange(-4,4,0.01)
X,Y=np.meshgrid(X,Y)
print(X,Y)
# R=np.sqrt(X**2 +Y**2)
# Z=np.sin(R)
Z=(1/(2*np.pi)*np.exp(-(X**2 +Y**2)/2))
ax.plot_surface(X,Y,Z,cmap='rainbow')
plt.savefig('gaosi.png',bbox_inches='tight')
#plt.show()

