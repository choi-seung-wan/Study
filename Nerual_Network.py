import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    if x<=0:
        return 0
    else:
        return 1

def sig_func(x):
    y=x>0
    return y.astype(np.uint8) #y의 데이터 저장 형태를 bool -> int (False=0, True=1)

def step_func(x):
    return np.array(x>0,dtype=np.uint8)

# a=np.arange(-5.0,5.0,0.1)
# y=step_func(a)
# plt.plot(a,y)
# plt.ylim(-0.1,1.1) #Y축 범위 지정(0.0-1.0)
# plt.show()

def sigmoid_func(x):
    return 1/(1+np.exp(-x))

# b=np.arange(-5.0,5.0,0.01)
# print(sigmoid_func(b))
# c=sigmoid_func(b)
# plt.plot(b,c)
# plt.ylim(-0.1,1.1)
# plt.show()

def Relu(x):
    return np.maximum(0,x)

c=np.arange(-10.0,5.0,0.1)
print(Relu(c))
d=Relu(c)
plt.plot(c,d)
plt.ylim(-0.1,1.1)
plt.show()