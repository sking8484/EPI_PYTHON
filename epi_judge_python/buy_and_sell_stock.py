from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    minPrice,maxProfit = float('inf'), 0.0

    for p in range(len(prices)):
        maxProfit = max(maxProfit, prices[p] - minPrice)
        minPrice = min(minPrice, prices[p])
    return maxProfit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
