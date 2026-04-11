from typing import Optional, List, Dict


# 定義圖形的節點結構
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    @staticmethod
    def cloneGraph(node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}

        def dfs(node: Optional['Node']):
            if node in old_to_new:
                return old_to_new[node]

            copy_node = Node(node.val)

            old_to_new[node] = copy_node

            for neighbor in node.neighbors:
                copy_node.neighbors.append(dfs(neighbor))
            return copy_node

        return dfs(node)


def build_graph(adj_list: List[List[int]]) -> Optional['Node']:
    """輔助函式：將鄰接列表轉為 Node 物件圖形"""
    if not adj_list:
        return None
    nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}
    for i, neighbors in enumerate(adj_list):
        nodes[i + 1].neighbors = [nodes[neigh] for neigh in neighbors]
    return nodes[1]


def get_adj_list(node: Optional['Node']) -> List[List[int]]:
    """輔助函式：將 Node 物件圖形轉回鄰接列表，方便 assert 比對"""
    if not node:
        return []
    visited = {}

    def dfs(n):
        if n.val in visited: return
        visited[n.val] = sorted([neigh.val for neigh in n.neighbors])
        for neigh in n.neighbors:
            dfs(neigh)

    dfs(node)
    return [visited[i] for i in sorted(visited.keys())]


def test_1():
    # 範例 1: 標準方形圖形 [[2,4],[1,3],[2,4],[1,3]]
    adj = [[2, 4], [1, 3], [2, 4], [1, 3]]
    root = build_graph(adj)
    cloned = Solution.cloneGraph(root)

    # 檢查值是否相同
    assert get_adj_list(cloned) == adj
    # 檢查是否為「深拷貝」(記憶體位址必須不同)
    assert cloned is not root


def test_2():
    # 範例 2: 只有一個節點
    adj = [[]]
    root = build_graph(adj)
    cloned = Solution.cloneGraph(root)
    assert get_adj_list(cloned) == adj
    assert cloned is not root


def test_3():
    # 範例 3: 空圖形
    assert Solution.cloneGraph(None) is None