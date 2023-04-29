import matplotlib.pyplot as plt
import numpy as np

max_plot_items = 15


# Функция выбирает точки, заданные пользователем или последние 15 точек, если условие не задано
def create_data(_iterator=None):
    with open("data.txt", "r") as file:
        xs, ys = [], []
        rd = file.readlines()
        _iterator = _iterator if _iterator else range(-max_plot_items, 0, 1)
        for i in _iterator:
            x, y = map(lambda p: float(p.strip()), rd[i].split(','))
            xs.append(x)
            ys.append(y)

        return xs, ys


# Функция создаёт график и рисует на нём среднюю линию всех выбранных значений
def create_plt(x, y):
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot(x, y)
    plt.axhline(y=np.nanmean(y), color="red")
    plt.show()


# Функция обрабатывает команды пользователя
def process_cmd(string):
    sp = [i.lower().strip() for i in string.split()]
    rng = None

    if sp[0] == 'select':
        if len(sp) == 3:
            rng = range(int(sp[1]), int(sp[2]))
        elif sp[1].isnumeric():
            rng = range(-int(sp[1]), 0, 1)
        elif sp[1] == "max":
            return

    return rng


if __name__ == "__main__":
    while True:
        create_plt(*create_data(process_cmd(input())))
