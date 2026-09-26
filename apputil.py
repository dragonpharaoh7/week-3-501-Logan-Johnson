import numpy as np
import pandas as pd
import seaborn as sns

URL = (
    'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/'
    'book/data/bellevue_almshouse_modified.csv'
)

df_bellevue = pd.read_csv(URL)


def fibonacci(n):
    """Return the nth Fibonacci number, where fibonacci(0) is 0."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def to_binary(number):
    """Return the binary representation of a non-negative integer."""
    if number < 2:
        return number
    return number % 2 + 10 * to_binary(number // 2)


def task_1():
    """Return column names sorted from least to most missing values."""
    df = df_bellevue.copy()
    print("Messy data: 'gender' has stray values ('?', 'g', 'h'); "
          "treating them as missing.")
    df['gender'] = df['gender'].replace(['?', 'g', 'h'], np.nan)
    missing = df.isna().sum().sort_values(kind='stable')
    return missing.index.tolist()


def task_2():
    """Return a data frame of total admissions for each year."""
    years = df_bellevue['date_in'].str.split('-').str[0].astype(int)
    return (
        years
        .value_counts()
        .sort_index()
        .rename_axis('year')
        .reset_index(name='total_admissions')
    )
