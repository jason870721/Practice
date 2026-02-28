from collections import deque
from typing import Optional
import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_binary_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


class Solution:
    @staticmethod
    def maxDepth(root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        fifo = [root]
        level = 0

        while fifo:
            size = len(fifo)
            for _ in range(size):
                node = fifo.pop(0)

                if node.left:
                    fifo.append(node.left)
                if node.right:
                    fifo.append(node.right)

            level += 1

        return level


@pytest.mark.parametrize(
    "values, expected",
    [
        # 測試 1: 空樹
        ([], 0),

        # 測試 2: 單一節點
        ([1], 1),

        # 測試 3: 完全平衡樹
        ([3, 9, 20, None, None, 15, 7], 3),

        # 測試 4: 左偏樹
        ([1, 2, None, 3, None, 4, None], 4),

        # 測試 5: 右偏樹
        ([1, None, 2, None, 3, None, 4], 4),

        # 測試 6: 不平衡樹
        ([1, 2, 3, 4, None, None, 5], 3),
    ],
)
def test_max_depth(values, expected):
    root = list_to_binary_tree(values)
    result = Solution.maxDepth(root)
    assert result == expected