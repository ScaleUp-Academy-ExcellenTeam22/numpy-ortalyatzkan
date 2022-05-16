import numpy as np


def compute_median(array: np.array):
    """
    A function that calculate the median.
    :param array: Array for compute.
    :return: Median of array.
    """
    return np.median(array)


if __name__ == '__main__':
    original_array = [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]]
    print(compute_median(original_array))
