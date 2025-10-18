from typing import Optional, Tuple
import pytest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linkedlist(nums: list[int]) -> Optional[ListNode]:
    """
    將 Python list 轉成 Linked List
    """
    dummy = ListNode()
    curr = dummy
    for n in nums:
        curr.next = ListNode(n)
        curr = curr.next
    return dummy.next


def linkedlist_to_list(head: Optional[ListNode]) -> list[int]:
    """
    將 Linked List 轉回 Python list
    """
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


class Solution:
    @staticmethod
    def reorderList(head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None
        curr = second
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        first = head
        second = prev

        while first and second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
        ([1, 2, 3, 4], [1, 4, 2, 3]),
        ([1], [1]),
        ([], []),
        ([1, 2], [1, 2]),
    ]
)
def test_reorder_list(nums, expected):
    head = list_to_linkedlist(nums)
    Solution.reorderList(head)
    result_list = linkedlist_to_list(head)
    assert result_list == expected
