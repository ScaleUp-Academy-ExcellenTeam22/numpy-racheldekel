import numpy as np


def create_3D_array(array_size: int):
    """
    function that create a 3D array with ones on a diagonal and zeros elsewhere.
    :param array_size: int for array size
    :return: 3D array with ones on a diagonal and zeros
    """
    return np.eye(array_size)


if __name__ == '__main__':
    print(create_3D_array(3))
