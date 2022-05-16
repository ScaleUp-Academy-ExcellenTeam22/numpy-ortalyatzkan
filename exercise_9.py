import numpy as np


def duplicate_matrices(first_matrix: np.array, second_matrix: np.array):
    """
    A function that multiply two given arrays of same size element-by-element.
    :param first_matrix:First matrix to multiplication.
    :param second_matrix:Second matrix to multiplication.
    :return:The result matrix.
    """
    return first_matrix*second_matrix


if __name__ == '__main__':
    first_array = np.array([1, 2, 3])
    second_array = np.array([4, 5, 6])
    print(duplicate_matrices(first_array, second_array))
