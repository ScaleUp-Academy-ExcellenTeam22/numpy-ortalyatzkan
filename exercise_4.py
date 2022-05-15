import numpy as np


def create_matrix() -> np.array:
    """
   A function that return a 10x10 matrix, in which the elements on the borders is equal to 1, and inside 0
    :return:  a 10x10 matrix, in which the elements on the borders is equal to 1, and inside 0
    """
    matrix = np.ones((10, 10))
    matrix[1:9, 1:9] = 0
    return matrix


if __name__ == '__main__':
    print(create_matrix())
