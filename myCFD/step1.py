import numpy as np
import matplotlib.pyplot as plt
import time, sys

# Define the domain
nx = 41
dx = 2 / (nx - 1)
nt = 100
dt = 0.025
c = 1

u = np.ones(nx)
u[int(0.5 / dx) : int(1 / dx + 1)] = 2
print(u)

# plt.plot(np.linspace(0, 2, nx), u)
# plt.show()
# plt.close()

un = np.ones(nx)

# Backward difference integration
for n in range(nt):
    un = u.copy()
    for i in range(1, nx):
        u[i] = un[i] - c * dt / dx * (un[i] - un[i - 1])
    u[0] = un[-1]

    plt.plot(np.linspace(0, 2, nx), u)
    # plt.savefig(f"test{n:03d}.png")
    # plt.close()

# plt.plot(np.linspace(0, 2, nx), u)
# plt.show()
# plt.close()
