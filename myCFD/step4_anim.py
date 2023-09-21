"""
==================
Animated line plot
==================

Output generated via `matplotlib.animation.Animation.to_jshtml`.
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import sympy as sp
from sympy.utilities.lambdify import lambdify

sp.init_printing(use_latex=True)

x, nu, t = sp.symbols("x nu t")
phi = sp.exp(-((x - 4 * t) ** 2) / (4 * nu * (t + 1))) + sp.exp(
    -((x - 4 * t - 2 * sp.pi) ** 2) / (4 * nu * (t + 1))
)
# phi

phi_prime = phi.diff(x)
# phi_prime

u = -2 * nu * (phi_prime / phi) + 4

ufunc = lambdify((t, x, nu), u)


# Define the domain
nx = 101
nt = 100
dx = 2 * np.pi / (nx - 1)
nu = 0.07
dt = dx * nu

x = np.linspace(0, 2 * np.pi, nx)
un = np.empty(nx)
t = 0
u = np.asarray([ufunc(t, x0, nu) for x0 in x])
u_analytical = np.asarray([ufunc(nt * dt, x0, nu) for x0 in x])

# plt.figure(figsize=(11, 7), dpi=100)
# plt.plot(x, u, marker='o', lw=2)
# plt.xlim([0, 2 * np.pi])
# plt.ylim([0, 10]);

fig, ax = plt.subplots()

ax.set_xlim([0, 2 * np.pi])
ax.set_ylim([0, 10])

(line,) = ax.plot(x, u, marker="o", lw=2, label="Computational")
(line2,) = ax.plot(x, u_analytical, label="Analytical")


def animate(i):
    u[1:-1] = (
        u[1:-1]
        - u[1:-1] * dt / dx * (u[1:-1] - u[:-2])
        + nu * dt / dx**2 * (u[2:] - 2 * u[1:-1] + u[:-2])
    )

    u[0] = (
        u[0]
        - u[0] * dt / dx * (u[0] - u[-2])
        + nu * dt / dx**2 * (u[1] - 2 * u[0] + u[-2])
    )
    u[-1] = u[0]

    t = i * dt

    u_analytical = np.asarray([ufunc(t, xi, nu) for xi in x])

    line.set_ydata(u)  # update the data.
    line2.set_ydata(u_analytical)  # update the data.
    return (
        line,
        line2,
    )


ani = animation.FuncAnimation(fig, animate, interval=20, blit=True, save_count=50)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()
