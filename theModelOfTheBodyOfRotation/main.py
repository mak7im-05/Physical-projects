import numpy as np
import matplotlib.pyplot as plt

R = int(input("Введите радиус:"))
V = int(input("Введите скорость центр масс:"))
t = np.linspace(0, 4 * np.pi, 500)

omega = V / R

x = V * t - R * np.sin(omega * t)
y = R - R * np.cos(omega * t)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Траектория движения точки на ободе")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()