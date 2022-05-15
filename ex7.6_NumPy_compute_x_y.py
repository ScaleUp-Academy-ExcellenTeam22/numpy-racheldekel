import numpy as np
import matplotlib.pyplot as plt


def compute_x_y_coordinates():
    """
    function that compute the x and y coordinates for points on a sine curve and plot the points using matplotlib
    :return: showing the plot
    """
    x = np.arange(0, 3 * np.pi, 0.2)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    compute_x_y_coordinates()
