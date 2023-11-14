import numpy as np

def sigmoid_func(x):
    return 1/(1+np.exp(-x))

def id_func(x):
    return x

def network():
    network={}
    network['W1']=np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
    network['b1']=np.array([0.1,0.2,0.3])
    network['W2']=np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
    network['b2']=np.array([0.1,0.2])
    network['W3']=np.array([[0.1,0.3],[0.2,0.4]])
    network['b3']=np.array([0.1,0.2])
    return network

def forward(network, x):
    W1,W2,W3=network['W1'],network['W2'],network['W3']
    b1,b2,b3=network['b1'],network['b2'],network['b3']
    a1=np.dot(x,W1)+b1
    z1=sigmoid_func(a1)
    a2=np.dot(z1,W2)+b2
    z2=sigmoid_func(a2)
    a3=np.dot(z2,W3)+b3
    y=id_func(a3)
    return y
# a=np.array([1,2,3,4])
# print(a)
# print(np.ndim(a))
# print(a.shape)
# print(a.shape[0])
# print(a.reshape(2,2))
#
# b=np.array([[1,2],[3,4],[5,6]])
# c=np.array([[1,2],[3,4]])
# print(b)
# print(np.ndim(b))
# print(b.shape)
# print(np.dot(b,c))

X=np.array([0.1,0.2])
W=np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
b=np.array([0.1,0.2,0.3])
Y=np.dot(X,W)+b
i=id_func(Y)
z=sigmoid_func(Y)
print(X.shape)
print(W.shape)
print(Y)
print(z)
print(i)

network=network()
x=np.array([1.0,0.5])
y=forward(network, x)
print(y)
