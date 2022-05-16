import numpy as np


def combine_array(first_array, second_array)->None:
    """
    A function that combine a one and a two dimensional array together and display their elements.
    :param first_array:First array to combine.
    :param second_array: Second array to combine.
    :return: None
    """
    for first_element, second_element in np.nditer([first_array, second_array]):
        print("%d:%d" % (first_element, second_element),)


if __name__ == '__main__':
    One_dimensional_array = ([0, 1, 2, 3])
    Two_dimensional_array = ([[0, 1, 2, 3], [4, 5, 6, 7]])
    print(combine_array(One_dimensional_array, Two_dimensional_array))
