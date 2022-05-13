from numpy import array


def create_vector():
    """
    function that create a vector with number from 0 to 20 and returns the numbers between 9 and 15 to negative once
    :return:
    """
    vector = array(range(21))
    vector[9:16] *= -1
    return vector


if __name__ == '__main__':
    print(create_vector())

