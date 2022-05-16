import numpy as np


def sort(l_id: np.array, l_height: np.array):
    """
    A function that sort the student id with increasing height of the students from given students id and height.
    :param l_id:List of id.
    :param l_height:List of height.
    :return:
    """
    result = np.lexsort((l_id, l_height))
    print(result)
    for i in result:
        print(l_id[i], l_height[i])


if __name__ == '__main__':
    list_id = np.array([1234344, 332233, 22333, 2233343, 11111, 6666])
    list_height = np.array([1.70, 1.52, 1.80, 1.90, 2.0, 2.1])
    sort(list_id, list_height)
