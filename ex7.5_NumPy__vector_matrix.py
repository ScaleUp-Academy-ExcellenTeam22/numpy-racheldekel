import numpy as np


def create_vector_to_matrix(matrix: np, vector: np):
    """
    function that add a vector to each row of a given matrix.
    :param matrix: given matrix
    :param vector: given vector
    :return:
    """
    for row in range(matrix.shape[0]):
        matrix[row] += vector
    return matrix


if __name__ == '__main__':
    matrix_from = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    vector_to = np.array([1, 1, 0])
    print(create_vector_to_matrix(matrix_from, vector_to))
