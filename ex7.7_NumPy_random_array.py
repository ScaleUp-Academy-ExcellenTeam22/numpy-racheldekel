import numpy as np


def create_random_array_swapping_first_last_rows(matrix: np):
    """
    function that create a 4x4 array with random values,
    now create a new array from the said array swapping first and last rows.
    :param matrix: a random matrix
    :return: new array from the said array swapping first and last rows
    """
    new_matrix = matrix[:-2:-1]
    new_matrix = np.vstack([new_matrix, matrix[1:-1:]])
    new_matrix = np.vstack([new_matrix, matrix[:1:]])
    return new_matrix


if __name__ == '__main__':
    original_matrix = np.random.randint(0, 100, (4, 4))
    print("Original array:")
    print(original_matrix)
    print("\nNew array after swapping first and last rows of the said array:")
    print(create_random_array_swapping_first_last_rows(original_matrix))
