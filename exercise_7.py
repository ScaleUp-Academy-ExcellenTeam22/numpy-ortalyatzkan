import numpy as np


def create_matrix() -> np.array:
    """
    A function that create a 4x4 array with random values,
     after the function create a new array from this array and swapping first and last rows.
    :return:The new array after the swapping.
    """
    new_matrix = np.random.rand(4, 4)
    print(new_matrix)
    new_matrix[[0, 3]] = new_matrix[[3, 0]]
    return new_matrix


if __name__ == '__main__':
    print(create_matrix())
