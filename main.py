import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from matplotlib import style
from random import random, randint


# Инициализация графика
style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

# Максимальное количество точек на графике
max_points = 10

# Среднее значение
avg = 0.5

# Список с точками
lines = [(0, random())]
# Счётчик кадров
p = 1


# Функция, обновляющая график
def animate(i):
    # Счётчик кадров
    global p
    xs = []
    ys = []

    # Убираем старую точку и добавляем новую
    if len(lines) > max_points:
        lines.pop(0)
    val = create_new_point()
    lines.append((p, val))
    p += 1

    # Записать новую точку в файл
    with open("data.txt", "a") as file:
        file.write(f"{p},{val}\n")

    # Выбрать n последних точек
    for k in range(len(lines)):
        x, y = lines[k]
        xs.append(float(x))
        ys.append(float(y))

    # print(create_plt(*create_data()))

    # Очистить график от старой информации
    ax1.clear()

    # Построить новый график.
    # Если новое значение > старого более чем на 50%, то оно отобразится красным цветом
    # Если нвоое значение лежит в пределах нормы, оно будет отображено зелёным цветом
    if val * 0.50 >= avg:
        ax1.plot(xs, ys, color="red")
    else:
        ax1.plot(xs, ys, color="green")



# Случайно создаёт новую точку
def create_new_point():
    if random() > 0.74:
        return random() * randint(2, 3)
    else:
        return random()


if __name__ == "__main__":
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()