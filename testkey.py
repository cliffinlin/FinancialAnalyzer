import matplotlib.pyplot as plt
import numpy as np

data = np.linspace(1, 100)
power = 0


def on_keyboard(event):
    global power
    if event.key == 'right':
        power += 1
    elif event.key == 'left':
        power -= 1

    plt.clf()
    plt.plot(data ** power)
    plt.draw()


# plt.plot(data**power)


# def on_keyboard(event):
#     global power
#     if event.key == 'right':
#         power += 1
#     elif event.key == 'left':
#         power -= 1
#
#     plt.clf()
#     plt.plot(data**power)
#     plt.draw()


def draw():
    global data
    global power

    data = np.linspace(1, 100)
    power = 0
    plt.plot(data ** power)

    plt.gcf().canvas.mpl_connect('key_press_event', on_keyboard)

    plt.show()
