import numpy as np
import matplotlib.pyplot as plt

# Определение функций
def line(x):
    return 2*x + 3

def parabola(x):
    return x**2

# Определение точек пересечения
x_values = np.linspace(-2, 4, 100)
y_line = line(x_values)
y_parabola = parabola(x_values)

# Границы интегрирования (найденные x=-1 и x=3)
x_fill = np.linspace(-1, 3, 100)
y_fill_line = line(x_fill)
y_fill_parabola = parabola(x_fill)

# Построение графика
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_line, label=r'$y = 2x + 3$', color='blue')
plt.plot(x_values, y_parabola, label=r'$y = x^2$', color='red')
plt.fill_between(x_fill, y_fill_line, y_fill_parabola, color='lightblue', alpha=0.5)  # Закрашенная область

# Оси
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Настройки графика
plt.xlabel("x")
plt.ylabel("y")
plt.title("График функций и ограниченная область")
plt.legend()
plt.grid()

# Отображение графика
plt.show()
