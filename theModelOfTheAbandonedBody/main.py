import numpy as np
import matplotlib.pyplot as plt

g = 9.81

v0 = float(input("Введите начальную скорость (м/с): "))
a = float(input("Введите угол броска (градусы): "))
h = float(input("Введите начальную высоту (м): "))

a_rad = np.radians(a)
t_flight = (v0 * np.sin(a) + np.sqrt((v0 * np.sin(a)) ** 2 + 2 * g * h)) / g
t = np.linspace(0, t_flight, num=500)
x = v0 * np.cos(a_rad) * t
y = h + v0 * np.sin(a_rad) * t - 0.5 * g * t ** 2

vx = v0 * np.cos(a_rad)
vy = v0 * np.sin(a_rad) - g * t

plt.plot(x, y, label='Траектория')
plt.xlabel('X (м)')
plt.ylabel('Y (м)')
plt.title('Траектория полета тела')
plt.legend()
plt.grid(True)
plt.show()

vx_dict = []
for i in range(500):
    vx_dict.append(vx)

plt.plot(t, vx_dict, label='Горизонтальная скорость')
plt.plot(t, vy, label='Вертикальная скорость')
plt.xlabel('Время (с)')
plt.ylabel('Скорость (м/с)')
plt.title('Графики скорости')
plt.legend()
plt.grid(True)
plt.show()

plt.plot(t, x, label='Горизонтальная координата')
plt.plot(t, y, label='Вертикальная координата')
plt.xlabel('Время (с)')
plt.ylabel('Координата (м)')
plt.title('Графики зависимости координат от времени')
plt.legend()
plt.grid(True)
plt.show()
