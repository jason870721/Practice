import pytest
from collections import deque
from typing import List, Optional


# 1. 樹節點定義 (保持不變)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 2. 建樹工具 (保持不變，支援 LeetCode 格式)
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


# 3. 妳要挑戰的實作類別
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def get_value(node):
            if not node:
                return 0
            left_gain = max(get_value(node.left), 0)
            right_gain = max(get_value(node.right), 0)

            current_path_sum = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, current_path_sum)

            return node.val + max(left_gain, right_gain)

        get_value(root)
        return self.max_sum




# 4. Pytest 測試案例
@pytest.mark.parametrize(
    "tree_vals, expected",
    [
        # Case 1: 簡單小樹 [1, 2, 3] -> 1+2+3 = 6
        ([1, 2, 3], 6),

        # Case 2: 包含負數的複雜樹 [-10, 9, 20, None, None, 15, 7]
        # 最大路徑是 15 + 20 + 7 = 42
        ([-10, 9, 20, None, None, 15, 7], 42),

        # Case 3: 全負數樹 -> 最大路徑就是值最大的那個節點
        ([-3], -3),
        ([-2, -1], -1),

        # Case 4: 路徑不經過根節點
        #       2
        #      / \
        #    -1   10
        #        /  \
        #      15    7
        # 最大路徑是 15 + 10 + 7 = 32
        ([2, -1, 10, None, None, 15, 7], 32),

        # Case 5: 混合正負數
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 48),
    ]
)
def test_max_path_sum(tree_vals, expected):
    root = list_to_binary_tree(tree_vals)
    solution = Solution()
    result = solution.maxPathSum(root)
    assert result == expected