import numpy as np


def create_matrix() -> np.array:
    """
    A function that create a three-dimension array with shape (300,400,5) and set to a variable.
     The function fill the array elements with values using unsigned integer (0 to 255).
    :return:matrix.
    """
    return np.random.randint(0, 256, (300, 400, 5), np.uint8)


if __name__ == '__main__':
    print(create_matrix())
