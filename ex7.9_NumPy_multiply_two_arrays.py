import numpy as np


def multiply_two_arrays():
    """
    function that multiply two given arrays of same size element-by-element.
    :return: multiply two given arrays of same size element-by-element
    """
    first_matrix = np.arange(16).reshape(4, 4)
    print("Array1:", first_matrix)
    sec_matrix = np.arange(16, 32).reshape(4, 4)
    print("Array2:", sec_matrix)
    return np.multiply(first_matrix, sec_matrix)


if __name__ == '__main__':
    print("\nMultiply said arrays of same size element-by-element:")
    print(multiply_two_arrays())

