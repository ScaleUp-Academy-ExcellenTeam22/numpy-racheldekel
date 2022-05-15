import numpy
import numpy as np


def replace_number(matrix: numpy.ndarray, number: int, sign: chr):
    """
    function that replace all numbers in a given array which is equal, less and greater to a given number.
    :param matrix: matrix
    :param number: number
    :param sign:
    :return:  array which is equal, less and greater to a given number.
    """
    if sign == "=":
        print(np.where(matrix == number, 100, matrix))
    elif sign == "<":
        print(np.where(matrix < number, 100, matrix))
    elif sign == ">":
        print(np.where(matrix > number, 100, matrix))


if __name__ == '__main__':
    array = np.random.randint(1000, size=16).reshape(4, 4)
    number_to_compare = 500
    replace_number(array, number_to_compare, "=")
    replace_number(array, number_to_compare, "<")
    replace_number(array, number_to_compare, ">")
