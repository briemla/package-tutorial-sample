from pandas import DataFrame


def add_one(number):
    return number + 1


def set_dataframes(data: DataFrame):
    data.iloc[:, 0] = 1
    return data
