import numpy as np


def remove_single_dimensional_entries(arr: np.array, axis_num: int) -> np.array:
    """
    A function that gets array and number and to remove single-dimensional entries from a specified shape.
    :param arr:The array from which it will be deleted.
    :param axis_num:Axis for delete.
    :return:Array after remove single-dimensional entries.
    """
    return np.squeeze(arr, axis=axis_num)


if __name__ == '__main__':
    array = np.ones((3, 1, 4))
    axis = 1
    print(remove_single_dimensional_entries(array, axis).shape)
