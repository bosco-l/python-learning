"""
1393. Capital Gain/Loss

Medium

https://leetcode.com/problems/capital-gainloss/description/
"""
import pandas as pd
import numpy as np


def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    stocks['trade_price'] = np.where(stocks['operation'] == 'Buy',
                                     -stocks['price'],
                                     stocks['price'])
    return stocks.groupby(['stock_name'], as_index=False).agg(capital_gain_loss=('trade_price', 'sum'))


if __name__ == '__main__':
    data = [
        {'stock_name': 'Leetcode', 'operation': 'Buy', 'operation_day': 1, 'price': 1000},
        {'stock_name': 'Corona Masks', 'operation': 'Buy', 'operation_day': 2, 'price': 10},
        {'stock_name': 'Leetcode', 'operation': 'Sell', 'operation_day': 5, 'price': 9000},
        {'stock_name': 'Handbags', 'operation': 'Buy', 'operation_day': 17, 'price': 30000},
        {'stock_name': 'Corona Masks', 'operation': 'Sell', 'operation_day': 3, 'price': 1010},
        {'stock_name': 'Corona Masks', 'operation': 'Buy', 'operation_day': 4, 'price': 1000},
        {'stock_name': 'Corona Masks', 'operation': 'Sell', 'operation_day': 5, 'price': 500},
        {'stock_name': 'Corona Masks', 'operation': 'Buy', 'operation_day': 6, 'price': 1000},
        {'stock_name': 'Handbags', 'operation': 'Sell', 'operation_day': 29, 'price': 7000},
        {'stock_name': 'Corona Masks', 'operation': 'Sell', 'operation_day': 10, 'price': 10000}
    ]
    df = pd.DataFrame(data)
    df = capital_gainloss(df)
