import numpy as np


def remove_single_dimensional(array_remove: np.array):
    """
    function that remove single-dimensional entries from a specified shape.
    :param array_remove:
    :return:
    """
    return np.squeeze(array_remove).shape


if __name__ == '__main__':
    array_to_remove = np.ones((3, 1, 4))
    print(remove_single_dimensional(array_to_remove))
