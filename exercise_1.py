import numpy as np


def create_vector():
    """
    A function that create a vector with values from 0 to 20 and print the vector
    after change the sign of the numbers in the range from 9 to 15 and print the vector
    :return:
    """
    vec = np.arange(0, 21)
    print(vec)
    vec[(vec < 16) & (vec > 8)] *= -1
    print(vec)


if __name__ == '__main__':
    create_vector()
