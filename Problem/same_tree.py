import pytest
from typing import Optional

# 樹節點定義
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 將 list 轉成二元樹
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

# 這是你要實作的 Same Tree 方法骨架
class Solution:
    @staticmethod
    def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return Solution.isSameTree(p.left, q.left) and Solution.isSameTree(p.right, q.right)


# 測試案例
@pytest.mark.parametrize(
    "tree1, tree2, expected",
    [
        # 兩棵空樹
        ([], [], True),

        # 單一節點相同
        ([1], [1], True),

        # 單一節點不同
        ([1], [2], False),

        # 完全相同的樹
        ([1, 2, 3], [1, 2, 3], True),

        # 結構相同但值不同
        ([1, 2, 3], [1, 3, 2], False),

        # 結構不同
        ([1, 2], [1, None, 2], False),

        # 更大不平衡樹
        ([1, 2, 3, None, 4], [1, 2, 3, None, 4], True),
    ]
)

def test_is_same_tree(tree1, tree2, expected):
    root1 = list_to_binary_tree(tree1)
    root2 = list_to_binary_tree(tree2)
    result = Solution.isSameTree(root1, root2)
    assert result == expected
