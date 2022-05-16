import numpy as np


def convert_array(first_array: np.array, second_array: np.array) -> np.array:
    """
    A function to convert (in sequence depth wise (along third axis)) two 1-D arrays into a 2-D array.
    :param first_array:First 1-D array.
    :param second_array:Second 1-D array.
    :return:2-D array.
    """
    return np.dstack((first_array, second_array))


if __name__ == '__main__':
    first_arr = ([10, 20, 30])
    second_arr = ([40, 50, 60])
    print(convert_array(first_arr, second_arr))
