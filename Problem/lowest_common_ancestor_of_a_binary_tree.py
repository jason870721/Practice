from collections import deque
import pytest
from typing import List, Optional


# 1. 樹節點定義
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 2. 建樹工具 (標準 LeetCode 格式)
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


# 3. 輔助工具：根據數值找到對應的 TreeNode 物件 (為了測試用)
def find_node(root: TreeNode, val: int) -> Optional[TreeNode]:
    if not root:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    if left: return left
    return find_node(root.right, val)


class Solution:
    @staticmethod
    def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = Solution.lowestCommonAncestor(root.left, p, q)
        right = Solution.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right


@pytest.mark.parametrize(
    "tree_vals, p_val, q_val, expected_val",
    [
        # Case 1: 標準範例 (兩邊分開)
        # root=3, p=5, q=1 -> LCA=3
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3),

        # Case 2: 堆疊 (其中一個節點就是另一個的祖先)
        # root=3, p=5, q=4 -> LCA=5 (因為 5 是 4 的父節點)
        ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5),

        # Case 3: 小樹
        # root=1, p=1, q=2 -> LCA=1
        ([1, 2], 1, 2, 1),
    ]
)
def test_lowest_common_ancestor(tree_vals, p_val, q_val, expected_val):
    # 1. 建樹
    root = list_to_binary_tree(tree_vals)

    # 2. 找出 p 和 q 的節點物件
    p_node = find_node(root, p_val)
    q_node = find_node(root, q_val)

    # 3. 執行解答
    result = Solution.lowestCommonAncestor(root, p_node, q_node)

    # 4. 驗證
    assert result is not None, "回傳值不應為 None"
    assert result.val == expected_val