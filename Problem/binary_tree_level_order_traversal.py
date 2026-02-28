from collections import deque
import pytest
from typing import List, Optional


# 樹節點定義
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 將 list 轉成二元樹（LeetCode 常見層序）
def list_to_binary_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
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
    def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        fifo = [root]

        while fifo:
            size = len(fifo)
            level = []

            for _ in range(size):
                node = fifo.pop(0)
                level.append(node.val)
                if node.left:
                    fifo.append(node.left)
                if node.right:
                    fifo.append(node.right)
            result.append(level)

        return result



@pytest.mark.parametrize(
    "input_tree, expected",
    [
        # 空樹
        ([], []),

        # 單一節點
        ([1], [[1]]),

        # 兩層
        ([3, 9, 20], [[3], [9, 20]]),

        # 標準 LeetCode 範例
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),

        # 不平衡樹
        ([1, 2, None, 3], [[1], [2], [3]]),
    ]
)
def test_level_order_traversal(input_tree, expected):
    root = list_to_binary_tree(input_tree)
    result = Solution.levelOrder(root)
    assert result == expected
