from typing import List
from collections import defaultdict, deque


class Solution:
    @staticmethod
    def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)

        state = [0] * numCourses

        def dfs(node):
            if state[node] == 1:
                return False  # cycle detected
            if state[node] == 2:
                return True  # already verified

            state[node] = 1  # mark as visiting

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            state[node] = 2  # mark as completed
            return True
            # check every node in case graph is disconnected
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


# ── Unit Tests ──────────────────────────────────────────────────────────────

def test_1():
    # 範例 1: 可以完成，2 門課，只需先修 0 再修 1
    assert Solution.canFinish(2, [[1, 0]]) is True


def test_2():
    # 範例 2: 無法完成，互相依賴形成環 0→1→0
    assert Solution.canFinish(2, [[1, 0], [0, 1]]) is False


def test_3():
    # 無先修條件，所有課程都能完成
    assert Solution.canFinish(5, []) is True


def test_4():
    # 線性鏈狀依賴 0→1→2→3，無環
    assert Solution.canFinish(4, [[1, 0], [2, 1], [3, 2]]) is True


def test_5():
    # 長鏈最後形成環 0→1→2→0
    assert Solution.canFinish(3, [[1, 0], [2, 1], [0, 2]]) is False


def test_6():
    # 多條獨立路徑匯聚，無環
    # 0→2, 1→2, 2→3
    assert Solution.canFinish(4, [[2, 0], [2, 1], [3, 2]]) is True


def test_7():
    # 只有環在子圖中，與其他節點無關
    # 節點 0,1 成環；節點 2,3 獨立
    assert Solution.canFinish(4, [[1, 0], [0, 1]]) is False


def test_8():
    # 單一節點，無先修
    assert Solution.canFinish(1, []) is True