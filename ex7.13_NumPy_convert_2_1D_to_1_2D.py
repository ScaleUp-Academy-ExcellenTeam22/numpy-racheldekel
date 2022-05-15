import numpy
import numpy as np


def convert_two_1D_to_one_2D_matrix(first_matrix: numpy.ndarray, sec_matrix: numpy.ndarray):
    """
    function that convert (in sequence depth wise (along third axis)) two 1-D arrays into a 2-D array.
    :param first_matrix:
    :param sec_matrix:
    :return:
    """
    return np.dstack((first_matrix, sec_matrix))


if __name__ == '__main__':
    first_array = (10, 20, 30)
    sec_array2 = (40, 50, 60)
    print(convert_two_1D_to_one_2D_matrix(first_array, sec_array2))
