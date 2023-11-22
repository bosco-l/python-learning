"""
https://leetcode.com/problems/second-highest-salary/description/
"""
import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    value = None

    list_values = sorted(employee['salary'].unique().tolist())
    if len(list_values) >= 2:
        value = list_values[-2]

    output = pd.DataFrame({'SecondHighestSalary': [value]})
    return output


if __name__ == '__main__':
    df = pd.DataFrame({'id': [1, 2, 3],
                       'salary': [0, 1, 1],
                       })
    second_highest_salary(df)
