import numpy as np
import matplotlib.pyplot as plt
# right now it can only handle fist order CDE

x = [0]
y = [0]
y2 = []
z = [1]

def fz(t, x, z):
    return -x

h = 0.001
N = 10000

for i in range(N):
    L1 = fz(x[-1], y[-1], z[-1])
    L2 = fz(x[-1] + 0.5 * h, y[-1] + 0.5 * h * z[-1], z[-1] + 0.5 * h * L1)
    L3 = fz(x[-1] + 0.5 * h, y[-1] + 0.5 * h * z[-1] + 0.25 * h ** 2 * L1, z[-1] + 0.5 * h * L2)
    L4 = fz(x[-1] + h, y[-1] + h * z[-1] + h ** 2 * 0.5 * L2, z[-1] + h * L3)
    if i <=4:
        y.append(y[-1] + h * z[-1] + h ** 2 / 6 * (L1 + L2 + L3))
        z.append(z[-1] + h / 6 * (L1 + 2 * L2 + 2 * L3 + L4))
        x.append(x[-1] + h)
        y2.append(y[-1])
    else:
        tempy = y[-1] + 24 / h * (55 * fz(x[-1], y[-1], z[-1])
                - 59 * fz(x[-2], y[-2], z[-2]) - 37 * fz(x[-3], y[-3], z[-3])
                - 9 * fz(x[-4], y[-4], z[-4]))
        tempy2 = fz(x[-1], tempy, z[-1])

plt.plot(x, y)
plt.title('Runge_Kutta')
tx = np.linspace(0, 10, 100)
ty = np.sin(tx)

plt.plot(tx, ty)
plt.title('True')
# plt.title('Nonlinear simple pendulum')
# plt.xlabel('t')
# plt.ylabel('theta')
# plt.legend()
plt.show()