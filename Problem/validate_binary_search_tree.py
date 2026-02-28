from collections import deque
import pytest
from typing import List, Optional
import math


# 1. 樹節點定義
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 2. 建樹工具 (已修正為標準 LeetCode 格式，不用動)
def list_to_binary_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


# 3. 解題區域 (請填寫這裡)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([(root, -math.inf, math.inf)])

        while queue:
            node, low, high = queue.popleft()

            if not (low < node.val < high):
                return False

            if node.left:
                queue.append((node.left, low, node.val))

            if node.right:
                queue.append((node.right, node.val, high))

        return True


@pytest.mark.parametrize(
    "input_tree, expected",
    [
        # Case 1: 有效
        #    2
        #   / \
        #  1   3
        ([2, 1, 3], True),

        # Case 2: 無效 (右子點 4 比根 5 小)
        #    5
        #   / \
        #  1   4
        ([5, 1, 4], False),

        # Case 3: 無效 (陷阱題：3 在右子樹，但比根 5 小)
        #      5
        #     / \
        #    1   4
        #       / \
        #      3   6
        ([5, 1, 4, None, None, 3, 6], False),
    ]
)
def test_is_valid_bst(input_tree, expected):
    root = list_to_binary_tree(input_tree)
    solver = Solution()
    result = solver.isValidBST(root)
    assert result == expected