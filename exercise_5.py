import numpy as np


def create_matrix(matrix: np.array, vec: np.array) -> np.array:
    """
    A function that get a vector and matrix and add a vector to each row of a given matrix.
    :param matrix:The matrix whose vector is added to its rows.
    :param vec:The Vector added rows.
    :return:The matrix After adding the vector.
    """
    for i in range(matrix.shape[0]):
        new_matrix[i, :] = matrix[i, :]+vec
    return new_matrix


if __name__ == '__main__':
    new_matrix = np.ones((2, 3))
    vector = np.array([1, 2, 3])
    print(new_matrix)
    print(create_matrix(new_matrix,vector))
