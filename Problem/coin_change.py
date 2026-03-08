from typing import List


class Solution:
    @staticmethod
    def coinChange(coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        if dp[amount] == float('inf'):
            return -1
        else:
            return int(dp[amount])


def test_1():
    assert Solution.coinChange([1, 2, 5], 11) == 3

def test_2():
    assert Solution.coinChange([2], 3) == -1

def test_3():
    assert Solution.coinChange([1], 0) == 0