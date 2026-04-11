from collections import deque
from typing import List


class Solution:
    @staticmethod
    def numIslands(grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        # def dfs(r, c):
        #     # 1. 檢查邊界條件與是否為陸地
        #     if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
        #         return
        #
        #     # 2. 將當前陸地「淹沒」成水，防止重複掃描
        #     grid[r][c] = '0'
        #
        #     # 3. 往四個方向繼續深度搜尋
        #     dfs(r + 1, c)  # 下
        #     dfs(r - 1, c)  # 上
        #     dfs(r, c + 1)  # 右
        #     dfs(r, c - 1)  # 左

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1

                    grid[r][c] = '0'

                    queue = deque([(r, c)])
                    while queue:
                        current_r, current_c = queue.popleft()

                        # 檢查四個方向
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = current_r + dr, current_c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                                queue.append((nr, nc))
                                grid[nr][nc] = '0'

        return count

def test_1():
    # 範例 1: 單一大型島嶼
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert Solution.numIslands(grid) == 1


def test_2():
    # 範例 2: 三個獨立島嶼
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert Solution.numIslands(grid) == 3


def test_3():
    # 範例 3: 完全沒有陸地
    grid = [
        ["0", "0", "0"],
        ["0", "0", "0"]
    ]
    assert Solution.numIslands(grid) == 0