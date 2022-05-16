import numpy as np
import matplotlib.pylab as plt


def show_graph() -> None:
    """
    A function which displays the graph of the points it gets.
    :return:None.
    """
    x_coordinate = np.arange(0, 3 * np.pi, 0.2)
    y_coordinate = np.sin(x_coordinate)
    plt.plot(x_coordinate, y_coordinate)
    plt.show()



if __name__ == '__main__':
    show_graph()
