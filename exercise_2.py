import numpy as np


def create_vector():
    """
    A function that create a vector of length 10 with values evenly distributed between 5 and 50
    :return: The vector that the function created
    """
    return np.linspace(5, 50, 10)


if __name__ == '__main__':
    print(create_vector())
