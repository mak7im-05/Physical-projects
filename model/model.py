import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

radius = float(input("Введите радиус: "))
speed = float(input("Введите скорость: "))

maxT = 2 * 2 * np.pi * radius / speed
time = np.linspace(0, maxT, 100)
x = speed * time - radius * np.sin(speed / radius * time + np.pi / 2)
y = radius * (1 - np.cos(speed / radius * time + np.pi / 2))

figure, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim((0, max(speed * time) + radius))
ax.set_ylim((-radius, 2 * radius + radius))
ax.set_aspect("equal")

theta = np.linspace(0, 2 * np.pi, 100)

def update(frame):
    ax.clear()
    ax.set_xlim((0, max(speed * time) + radius))
    ax.set_ylim((-radius, 2 * radius + radius))
    ax.set_aspect("equal")
    ax.grid(True)

    ax.plot(x[:frame], y[:frame], lw=2, label="Траектория")

    angle = -speed / radius * time[frame]
    x_wheel = radius * np.cos(theta) + speed * time[frame]
    y_wheel = radius * np.sin(theta) + radius
    ax.plot(x_wheel, y_wheel, "b", lw=2, label="Обод")

    x_point_on_wheel = radius * np.cos(angle + np.pi) + speed * time[frame]
    y_point_on_wheel = radius * np.sin(angle + np.pi) + radius
    ax.plot(x_point_on_wheel, y_point_on_wheel, "ro")

    ax.legend()


animation = FuncAnimation(figure, update, frames=len(time), interval=20 * (2 / speed))
plt.show()
