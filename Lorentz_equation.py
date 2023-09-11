import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ... rest of the code ...



# define Lorentz equation
# DX/dt = - sigma * (X - Y)
# DY/dt = gama * X - Y - X * Z
# DZ/dt = - beta * Z + X * Y

sigma = 10
gamma = 25
beta = 8/3
t = [0]
x = [1]
y = [0]
z = [0]
h = 0.01
N = 100000

def FX(X, Y, Z):
    return - sigma * (X - Y)

def FY(X, Y, Z):
    return gamma * X - Y - X * Z

def FZ(X, Y, Z):
    return - beta * Z + X * Y

def main():
    for i in range(N):
        K1 = FX(x[-1], y[-1], z[-1])
        L1 = FY(x[-1], y[-1], z[-1])
        M1 = FZ(x[-1], y[-1], z[-1])

        K2 = FX(x[-1] + h * K1 / 2, y[-1] + h * L1 / 2, z[-1] + h * M1 / 2)
        L2 = FY(x[-1] + h * K1 / 2, y[-1] + h * L1 / 2, z[-1] + h * M1 / 2)
        M2 = FZ(x[-1] + h * K1 / 2, y[-1] + h * L1 / 2, z[-1] + h * M1 / 2)

        K3 = FX(x[-1] + h * K2 / 2, y[-1] + h * L2 / 2, z[-1] + h * M2 / 2)
        L3 = FY(x[-1] + h * K2 / 2, y[-1] + h * L2 / 2, z[-1] + h * M2 / 2)
        M3 = FZ(x[-1] + h * K2 / 2, y[-1] + h * L2 / 2, z[-1] + h * M2 / 2)

        K4 = FX(x[-1] + h * K3, y[-1] + h * L3, z[-1] + h * M3)
        L4 = FY(x[-1] + h * K3, y[-1] + h * L3, z[-1] + h * M3)
        M4 = FZ(x[-1] + h * K3, y[-1] + h * L3, z[-1] + h * M3)

        x.append(x[-1] + h / 6 * (K1 + 2 * K2 + 2 * K3 + K4))
        y.append(y[-1] + h / 6 * (L1 + 2 * L2 + 2 * L3 + L4))
        z.append(z[-1] + h / 6 * (M1 + 2 * M2 + 2 * M3 + M4))
        t.append(t[-1] + h)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, label='parametric curve')
    plt.show()

main()















