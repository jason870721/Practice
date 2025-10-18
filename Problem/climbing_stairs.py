class Solution:
    @staticmethod
    def climbStairs(n: int) -> int:
        if n == 1:
            return 1
        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, a + b
        return b


def test_1():
    assert Solution.climbStairs(2) == 2

def test_2():
    assert Solution.climbStairs(3) == 3

def test_3():
    assert Solution.climbStairs(4) == 5