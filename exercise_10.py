import numpy as np


def sort_array_along_first_axis(array: np.array) -> np.array:
    """
    A function that gets an array and sort an along the first axis of this array.
    :param array:Array to sort.
    :return:The Sorted array.
    """
    return np.sort(array, axis=0)


def sort_array_along_last_axis(array: np.array) -> np.array:
    """
    A function that gets an array and sort an along the last axis of this array.
    :param array:Array to sort.
    :return:The Sorted array.
    """
    return np.sort(array, axis=1)


if __name__ == '__main__':
    arr = np.array([[2, 1], [4, 6]])
    print(sort_array_along_first_axis(arr))
    print(sort_array_along_last_axis(arr))
