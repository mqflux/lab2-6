import matplotlib.pyplot as plt
import matplotlib.animation as animation
import asyncio
import sys
import time
from matplotlib import style
from random import random


style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

max_points = 10

lines = [(0, random())]
p = 1


def animate(i):
    global p
    xs = []
    ys = []

    if len(lines) > 15:
        lines.pop(0)
    val = random()
    lines.append((p, val))
    p += 1

    with open("data.txt", "a") as file:
        file.write(f"{p},{val}\n")

    for k in range(len(lines)):
        x, y = lines[k]
        xs.append(float(x))
        ys.append(float(y))

    # print(create_plt(*create_data()))

    ax1.clear()

    if max(val, lines[-2][1]) * 0.50 >= min(val, lines[-2][1]):
        ax1.plot(xs, ys, color="red")
    else:
        ax1.plot(xs, ys, color="green")


if __name__ == "__main__":
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()