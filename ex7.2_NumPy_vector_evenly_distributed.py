import numpy as np


def create_vector_evently_distributed(length, min_value, max_value):
    """
    function that create a vector of length 10 with values evenly distributed between 5 and 50
    :return: vector with length between min_value to max_value.
    """
    return np.linspace(min_value, max_value, length)


if __name__ == '__main__':
    print(create_vector_evently_distributed(10, 5, 50))
