import numpy as np


def count_number_of_days_of_january():
    return np.datetime64('2022-02-01')-np.datetime64('2022-01-01')


if __name__ == '__main__':
    print(count_number_of_days_of_january())
