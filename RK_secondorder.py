from numpy import *
import matplotlib.pyplot as plt

# pendulum larger than 5°
def fz(t, theta, z):
    # time, angle, angular velocity
    return -sin(theta)

# t = 0, theta = 10°
# t = 0, w = 0
# release the pendulum at an angle of 10 ° without initial velocity
t = [0]
theta = [10/180*pi]
w = [0]

# h:step N:total number h*step:moving distance
h = 0.01
N = 2000

for i in range(N):
    L1 = fz(t[-1], theta[-1], w[-1])
    L2 = fz(t[-1] + 0.5 * h, theta[-1] + 0.5 * h * w[-1], w[-1] + 0.5 * h * L1)
    L3 = fz(t[-1] + 0.5 * h, theta[-1] + 0.5 * h * w[-1] + 0.25 * h ** 2 * L1, w[-1] + 0.5 * h * L2)
    L4 = fz(t[-1] + h, theta[-1] + h * w[-1] + h ** 2 * 0.5 * L2, w[-1] + h * L3)

    theta.append(theta[-1] + h * w[-1] + h ** 2 / 6 * (L1 + L2 + L3))
    w.append(w[-1] + h / 6 * (L1 + 2 * L2 + 2 * L3 + L4))
    t.append(t[-1] + h)

plt.plot(t, theta)
plt.title('Nonlinear simple pendulum')
plt.xlabel('t')
plt.ylabel('theta')
# plt.legend()
plt.show()
