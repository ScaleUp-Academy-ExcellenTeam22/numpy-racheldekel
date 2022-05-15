import numpy as np


def sort_array_axis(array: np.array, axis: str):
    """
    function that sort an along the first, last axis of an array
    :param array:
    :param axis:
    :return:
    """
    if axis == 'x':
        return np.sort(array, axis=0)
    if axis == 'y':
        x = np.sort(array, axis=0)
        return np.sort(x, axis=1)


if __name__ == '__main__':
    array_sort = np.array([[4, 6], [2, 1]])
    print("Original array: ")
    print(array_sort)
    print("Sort along the first axis: ")
    print(sort_array_axis(array_sort, 'x'))
    print("Sort along the last axis: ")
    print(sort_array_axis(array_sort, 'y'))
