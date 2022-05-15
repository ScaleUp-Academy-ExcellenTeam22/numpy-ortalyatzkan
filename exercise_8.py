import numpy as np


def replace_equal_number(arr: np.array, num_comp: int, num_replace: int) -> np.array:
    """
    A function that gets an array and a number and replaces all the numbers in the array that are equal to the number.
    :param arr:Array for replace.
    :param num_comp:Number for comparison.
    :param num_replace:Number replace it with all the numbers for which the condition is correct.
    :return:Array after replace.
    """
    return np.where(arr == num_comp, num_replace, arr)


def replace_smaller_number(arr: np.array, num_comp: int, num_replace: int) -> np.array:
    """
    A function that gets an array and a number and replaces all the numbers in the array that are smaller to the number.
    :param arr:Array for replace.
    :param num_comp:Number for comparison.
    :param num_replace:Number replace it with all the numbers for which the condition is correct.
    :return:Array after replace.
    """
    return np.where(arr < num_comp, num_replace, arr)


def replace_greater_number(arr: np.array, num_comp: int, num_replace: int) -> np.array:
    """
    A function that gets an array and a number and replaces all the numbers in the array that are greater to the number.
    :param arr:Array for replace.
    :param num_comp:Number for comparison.
    :param num_replace:Number replace it with all the numbers for which the condition is correct.
    :return:Array after replace.
    """
    return np.where(arr > num_comp, num_replace, arr)


if __name__ == '__main__':
    new_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(new_arr)
    print(replace_equal_number(new_arr, 3, 0))
    print(replace_smaller_number(new_arr, 3, 0))
    print(replace_greater_number(new_arr, 3, 0))
