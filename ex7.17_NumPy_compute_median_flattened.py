import numpy as np


def compute_median_flattened():
    """
    function that compute the median of flattened given array
    :return:
    """
    array = np.arange(12)
    median = np.median(array)
    print(median)


if __name__ == '__main__':
    compute_median_flattened()
