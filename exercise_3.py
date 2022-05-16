import numpy as np


def get_num_of_columns_and_rows(matrix: np.array) -> tuple:
    """
    A function that find the number of rows and columns of matrix that it gets.
    :param matrix:Matrix for checking the num of columns and rows.
    :return:Tuple of num of columns and rows.
    """
    return matrix.shape


if __name__ == '__main__':
    new_matrix = np.random.rand(5,10)
    print(get_num_of_columns_and_rows(new_matrix))
