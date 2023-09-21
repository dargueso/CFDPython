"""
==================
Animated line plot
==================

Output generated via `matplotlib.animation.Animation.to_jshtml`.
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Define the domain
nx = 41
dx = 2 / (nx - 1)
nt = 25
nu = 0.3
sigma = 0.2
dt = sigma * dx**2 / nu

u = np.ones(nx)
u[int(0.5 / dx) : int(1 / dx + 1)] = 2


fig, ax = plt.subplots()

x = np.linspace(0, 2, nx)
(line,) = ax.plot(x, u)


def animate(i):
    u[1:-1] = u[1:-1] + nu * dt / dx**2 * (u[2:] - 2 * u[1:-1] + u[:-2])

    line.set_ydata(u)  # update the data.
    return (line,)


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
