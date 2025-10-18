from typing import List

class Solution:
    @staticmethod
    def maxProfit(prices: List[int]) -> int:
        min_price = float('inf')
        profit = 0

        for current in prices:
            min_price = min(current, min_price)
            temp = current - min_price
            profit = max(profit, temp)

        return profit


def test_1():
    assert Solution.maxProfit(prices = [7,1,5,3,6,4]) == 5

def test_2():
    assert Solution.maxProfit(prices = [7,6,4,3,1]) == 0

# def test_3():
#     assert Solution.maxProfit(10) == False
