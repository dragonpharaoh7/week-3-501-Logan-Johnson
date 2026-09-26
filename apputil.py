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
    """Return the binary representation of a non-negative integer as a str."""
    if number < 2:
        return str(number)
    return to_binary(number // 2) + str(number % 2)


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


def task_3():
    """Return the average age for each gender."""
    print("Messy data: 'gender' has stray values ('?', 'g', 'h') and "
          "'age' has missing values; both are excluded from the averages.")
    gender = df_bellevue['gender'].replace(['?', 'g', 'h'], np.nan)
    return df_bellevue.groupby(gender)['age'].mean()


def task_4():
    """Return the 5 most common professions, most common first."""
    print("Messy data: 'profession' has missing values, which are not "
          "counted.")
    return df_bellevue['profession'].value_counts().head(5).index.tolist()
