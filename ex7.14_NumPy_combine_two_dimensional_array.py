import numpy as np


def combinetwo_dimensional_array(first_array: np.array, sec_array: np.array):
    """
    function that combine a one and a two dimensional array together and display their elements.
    :param first_array:
    :param sec_array:
    :return:
    """
    for x, y in np.nditer([first_array, sec_array]):
        print(f"{x}:{y}")


if __name__ == '__main__':
    array_1D = np.array([0, 1, 2, 3])
    array_2D = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
    combinetwo_dimensional_array(array_1D, array_2D)
