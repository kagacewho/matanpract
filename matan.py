import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 6*x - x**2

x = np.linspace(0, 6, 100)
y = f(x)

# Построение графика
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'y = 6x - x^2', color='black')
plt.fill_between(x, y, 0, where=(y>=0), color='white', alpha=0.5)  # Закрашенная область
plt.axhline(0, color='black', linewidth=1)  # Ось Ox
plt.axvline(0, color='black', linewidth=1)  # Ось Oy

# Настройки графика
plt.xlabel("Ось Ox")
plt.ylabel("Ось Oy")
plt.title("График функции и ограниченная область")
plt.legend()
plt.grid()

plt.show()

