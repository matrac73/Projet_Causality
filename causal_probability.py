from numpy.random import randn
import matplotlib.pyplot as plt

def x():
  return -5 + randn()

def y():
  return 5 + randn()

def z(x, y):
  return x + y + randn()

def sample():
  x_ = x()
  y_ = y()
  z_ = z(x_, y_)
  return x_, y_, z_

X, Y, Z = [], [], []
for i in range(10000):
    value = sample()
    X.append(value[0])
    Y.append(value[1])
    Z.append(value[2])

plt.hist(X, 20, alpha=0.7)
plt.hist(Y, 20, alpha=0.7)
plt.hist(Z, 20, alpha=0.7)
plt.figure()

plt.scatter(X,Y, color='r', alpha=0.1)
plt.show()