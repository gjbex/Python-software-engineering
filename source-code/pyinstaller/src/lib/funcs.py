import pandas as pd


def sum_columns(input_file):
    df = pd.read_csv(input_file)
    print(df.sum())

def prod_columns(input_file):
    df = pd.read_csv(input_file)
    print(df.prod())
