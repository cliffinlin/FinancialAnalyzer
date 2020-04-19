from configparser import ConfigParser

import matplotlib.pyplot as plt
import numpy as np

parser = ConfigParser()
parser.read('config.ini')
index = parser.getint('download', 'index')

parser.set('download', 'index', index)
with open('config.ini', 'w') as configfile:
    parser.write(configfile)

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
