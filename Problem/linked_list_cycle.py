from typing import Optional, Tuple
from xml.sax.handler import feature_string_interning

import pytest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linkedlist(nums: list[int]) -> Tuple[Optional[ListNode], list[ListNode]]:
    dummy = ListNode()
    curr = dummy
    nodes = []
    for n in nums:
        node = ListNode(n)
        nodes.append(node)
        curr.next = node
        curr = curr.next
    return dummy.next, nodes


class Solution:
    @staticmethod
    def hasCycle(head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


@pytest.mark.parametrize(
    "nums, make_cycle_index, expected",
    [
        # 不成環
        ([3, 2, 0, -4], None, False),
        ([1, 2], None, False),
        ([], None, False),

        # 成環
        ([3, 2, 0, -4], 1, True),  # 尾節點連回 index 1
        ([1, 2], 0, True),         # 尾節點連回 index 0
    ]
)
def test_linked_list_cycle(nums, make_cycle_index, expected):
    head, nodes = list_to_linkedlist(nums)

    if make_cycle_index is not None and nodes:
        nodes[-1].next = nodes[make_cycle_index]

    result = Solution.hasCycle(head)

    assert result == expected
