import numpy as np


def create_matrix(row_col_matrix):
    """
    function that find the number of rows and columns of a given matrix
    :param row_col_matrix:
    :return:
    """
    return row_col_matrix.shape


if __name__ == '__main__':
    matrix = np.arange(1, 10).reshape((3, 3))

    row, col = create_matrix(matrix)
    print(row, col)
