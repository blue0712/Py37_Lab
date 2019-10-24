import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
x = np.arange(0, 2 * np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x + i / 5.0))
    return line,


def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,


ani = animation.FuncAnimation(fig, animate, np.arange(1, 40000), init_func=init,
                              interval=60, blit=True)
plt.show()