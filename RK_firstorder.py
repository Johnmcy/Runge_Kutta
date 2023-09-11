import matplotlib.pyplot as plt
from numpy import *

# dy/dx = -sin(x)
def f(x, y):
    return -sin(x)

# initial condition when x = 0, y = 1
x = [0]
y = [1]

# h:step N:total number
h = 0.01
N = 1000

for i in range(N):
    K1 = f(x[-1], y[-1])
    K2 = f(x[-1] + 0.5 * h, y[-1] + 0.5 * h * K1)
    K3 = f(x[-1] + 0.5 * h, y[-1] + 0.5 * h * K2)
    K4 = f(x[-1] + h, y[-1] + h * K3)
    x.append(x[-1] + h)
    y.append(y[-1] + h/6 * (K1 + 2 * K2 + 2 * K3 + K4))

plt.plot(x, y)
plt.title('The original function of y = -sin(x)')
plt.xlabel('x')
plt.ylabel('y')
# plt.legend()
plt.show()




