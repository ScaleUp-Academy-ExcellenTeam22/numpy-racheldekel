import numpy as np


def sort_student_id():
    """
    function sort the student id with increasing height of the students from given students id and height.
    Print the integer indices that describes the sort order by multiple columns and the sorted data.
    :return:
    """
    student_id_array = np.array([1, 2, 3, 4, 5, 6, 7])
    student_height_array = np.array([80., 85., 85., 81., 88., 84., 82.0])
    sort_height = np.lexsort((student_id_array, student_height_array))
    for element in sort_height:
        print(student_id_array[element], student_height_array[element])


if __name__ == '__main__':
    sort_student_id()
