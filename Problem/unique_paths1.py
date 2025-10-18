from typing import List

class Solution:
    @staticmethod
    def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        # 初始化起點
        obstacleGrid[0][0] = 1

        # 初始化最上排
        for j in range(1, cols):
            if obstacleGrid[0][j] == 1:  # 遇到障礙物
                obstacleGrid[0][j] = 0
            else:
                obstacleGrid[0][j] = obstacleGrid[0][j - 1]

        # 初始化最左排
        for i in range(1, rows):
            if obstacleGrid[i][0] == 1:  # 遇到障礙物
                obstacleGrid[i][0] = 0
            else:
                obstacleGrid[i][0] = obstacleGrid[i - 1][0]

        # DP 從 (1,1) 開始
        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]

        return obstacleGrid[rows - 1][cols - 1]



def test_1():
    assert Solution.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]) == 2

def test_2():
    assert Solution.uniquePathsWithObstacles([[0,1],[0,0]]) == 1

# def test_3():
#     assert Solution.uniquePaths(3, 3) == 6
