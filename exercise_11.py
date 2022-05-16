import numpy as np


def build_identity_matrix(size_matrix: int) -> np.array:
    """
    A function that gets a size and returns the identity matrix in the size sent.
    :param size_matrix:Size of matrix.
    :return:The identity matrix in the size sent.
    """
    return np.eye(size_matrix)


if __name__ == '__main__':
    size = 3
    print(build_identity_matrix(size))
