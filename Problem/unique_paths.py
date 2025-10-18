class Solution:
    def uniquePaths(m: int, n: int) -> int:
        # matrix = [[1 for _ in range(n)] for _ in range(m)]
        # for i in range(1, m):
        #     for j in range(1, n):
        #         matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        # return matrix[m-1][n-1]

        a = max(m, n)
        b = min(m, n)
        arr = [1 for _ in range(a)]
        for i in range(1, b):
            for j in range(1, a):
                arr[j] += arr[j - 1]

        return arr[-1]




def test_1():
    assert Solution.uniquePaths(3,7) == 28

def test_2():
    assert Solution.uniquePaths(3,2) == 3

def test_3():
    assert Solution.uniquePaths(3,3) == 6