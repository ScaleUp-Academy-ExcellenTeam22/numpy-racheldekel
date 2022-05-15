import numpy as np
import nptyping


def sort_by_student_id_and_height(student_id: nptyping.ndarray,
                                  student_height: nptyping.ndarray):
    """
    function that compute the median of flattened given array.
    Note: First array elements raised to powers from second array
    :param student_id:
    :param student_height:
    :return:
    """
    return np.lexsort((student_id, student_height))


if __name__ == '__main__':
    student_id_array = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
    student_height_array = np.array([40., 42., 45., 41., 38., 40., 42.0])
    indices = sort_by_student_id_and_height(student_id_array, student_height_array)
    print("Sorted indices:")
    print(indices)
    print("Sorted data:")
    for n in indices:
        print(student_id_array[n], student_height_array[n])
