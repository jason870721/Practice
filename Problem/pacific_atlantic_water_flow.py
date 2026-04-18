from typing import List
from collections import deque


class Solution:
    @staticmethod
    def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(starts):
            visited = set(starts)
            queue = deque(starts)
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return visited

        pacific_starts = [(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)]
        atlantic_starts = [(r, rows - 1) for r in range(rows)] + [(rows - 1, c) for c in range(cols)]

        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)

        return [[r, c] for r, c in pacific & atlantic]

# ── Unit Tests ──────────────────────────────────────────────────────────────

def test_1():
    # 標準範例
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]
    result = Solution.pacificAtlantic(heights)
    expected = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    assert sorted(result) == sorted(expected)


def test_2():
    # 1x1 矩陣，唯一格子同時接觸兩個大洋
    heights = [[1]]
    result = Solution.pacificAtlantic(heights)
    assert sorted(result) == [[0, 0]]


def test_3():
    # 1xN，所有格子都能到達兩個大洋
    heights = [[1, 2, 3]]
    result = Solution.pacificAtlantic(heights)
    assert sorted(result) == sorted([[0, 0], [0, 1], [0, 2]])


def test_4():
    # 全部高度相同，所有格子都能到達兩個大洋
    heights = [
        [1, 1],
        [1, 1]
    ]
    result = Solution.pacificAtlantic(heights)
    assert sorted(result) == sorted([[0,0],[0,1],[1,0],[1,1]])


def test_5():
    # 高度遞增，只有右下角能同時到達兩個大洋
    heights = [
        [1, 2],
        [3, 4]
    ]
    result = Solution.pacificAtlantic(heights)
    assert sorted(result) == sorted([[0,1],[1,0],[1,1]])