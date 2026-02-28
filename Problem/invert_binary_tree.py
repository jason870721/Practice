from collections import deque

import pytest
from typing import Optional

# 樹節點定義
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 將 list 轉成二元樹（LeetCode 常見層序）
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


# 將二元樹轉回 list（方便測試比對）
def binary_tree_to_list(root: Optional[TreeNode]) -> list[Optional[int]]:
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # 移除尾端多餘的 None
    while result and result[-1] is None:
        result.pop()

    return result

class Solution:
    @staticmethod
    def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left
        Solution.invertTree(root.left)
        Solution.invertTree(root.right)

        return root

# 測試案例
@pytest.mark.parametrize(
    "input_tree, expected_tree",
    [
        # 空樹
        ([], []),

        # 單一節點
        ([1], [1]),

        # 只有左子樹
        ([1, 2], [1, None, 2]),

        # 只有右子樹
        ([1, None, 2], [1, 2]),

        # 完整二元樹
        ([1, 2, 3], [1, 3, 2]),

        # 不平衡樹
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
    ]
)
def test_invert_binary_tree(input_tree, expected_tree):
    root = list_to_binary_tree(input_tree)
    inverted = Solution.invertTree(root)
    result = binary_tree_to_list(inverted)
    assert result == expected_tree
