from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "null"

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")

        return ",".join(result)


        #------------------DFS
        # if not root:
        #     return "null"
        #
        # left_serialized = self.serialize(root.left)
        # right_serialized = self.serialize(root.right)
        #
        # return f"{root.val},{left_serialized},{right_serialized}"

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "null":
            return None

        values = iter(data.split(','))

        root_val = next(values)
        root = TreeNode(int(root_val))

        queue = deque([root])

        while queue:
            node = queue.popleft()

            try:
                left_val = next(values)
                if left_val != "null":
                    node.left = TreeNode(int(left_val))
                    queue.append(node.left)

                right_val = next(values)
                if right_val != "null":
                    node.right = TreeNode(int(right_val))
                    queue.append(node.right)
            except StopIteration:
                break

        return root



        #-------------------DFS
        # values = iter(data.split(','))
        #
        # def dfs():
        #     val = next(values)
        #
        #     if val == "null":
        #         return None
        #
        #     node = TreeNode(int(val))
        #
        #     node.left = dfs()
        #     node.right = dfs()
        #     return node
        #
        # return dfs()


# --- 以下是供你測試用的 pytest 測項 ---

import pytest


@pytest.mark.parametrize(
    "values",
    [
        [1, 2, 3, None, None, 4, 5],
        [1],
        [],
        [1, 2],
        [1, None, 2, None, 3],  # 右偏樹
    ],
)
def test_codec(values):
    # 這是一個輔助函式，用來把你的 list 轉成樹（你可以沿用你自己寫的 list_to_binary_tree）
    def build_tree(vals):
        if not vals: return None
        it = iter(vals)
        root = TreeNode(next(it))
        queue = deque([root])
        while queue:
            node = queue.popleft()
            try:
                val = next(it)
                if val is not None:
                    node.left = TreeNode(val)
                    queue.append(node.left)
                val = next(it)
                if val is not None:
                    node.right = TreeNode(val)
                    queue.append(node.right)
            except StopIteration:
                break
        return root

    codec = Codec()
    root = build_tree(values)

    # 測試流程：樹 -> 字串 -> 樹
    serialized_data = codec.serialize(root)
    deserialized_root = codec.deserialize(serialized_data)

    # 驗證最後序列化回來的結果是否與第一次一致
    assert codec.serialize(deserialized_root) == serialized_data