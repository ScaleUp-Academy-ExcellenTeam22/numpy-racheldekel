import numpy as np


def create_matrix_zero_one():
    """
  function that create a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0
    :return: 10x10 matrix with one's outside and inside zeros.
    """
    matrix = np.ones((10, 10))
    matrix[1:-1, 1:-1] = 0
    return matrix


if __name__ == '__main__':
    print(create_matrix_zero_one())
