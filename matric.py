import numpy as np
import matplotlib.pyplot as plt
# 矩阵乘法是周期性的，周期d=3
# a=np.array([[0,0,0.5,0.5,0,0],[0,0,0.5,0,0.5,0],[0,0,0,0,0,1],[0,0,0,0,0,1],[0,0,0,0,0,1],[0.5,0.5,0,0,0,0]])
# print(a)
# b=np.dot(a,a)
# print(b)
# c=np.dot(b,a)
# print(c)
# d=np.dot(c,a)
# print(d)
# e=np.dot(d,a)
# print(e)
# f=np.dot(e,a)
# print(f)
# g=np.dot(f,a)
# print(g)
# h=np.dot(g,a)
# print(h)


a=np.array([[0.8,0.2],[0.6,0.4]])
b=a
print(a)
print(b)
x1=[]
y1=[]
x2=[]
y2=[]
for i in range(0,10):
    b=np.dot(b,a)
    x1.append(i)
    y1.append(b[0][0])

    x2.append(i)
    y2.append(b[1][0])
    print(b[0][0]+b[0][1])
    print(b)
    # plt.plot([i], [b[0][0]], 'go-')
    # plt.plot([i], [b[1][0]], 'ks')
    # print(b)
plt.plot(x1, y1, 'go-')
plt.plot(x2,y2,'--')
plt.show()