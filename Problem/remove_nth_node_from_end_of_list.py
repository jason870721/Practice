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
    def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        for _ in range(n + 1):
            if fast is None:
                return head
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next


@pytest.mark.parametrize(
    "nums, n, expected",
    [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),  # 移除倒數第 2 個
        ([1], 1, []),                         # 移除唯一節點
        ([1, 2], 1, [1]),                     # 移除倒數第 1 個
        ([1, 2], 2, [2]),                     # 移除倒數第 2 個
        ([], 1, []),                          # 空鏈表
    ]
)
def test_remove_nth_from_end(nums, n, expected):
    head = list_to_linkedlist(nums)

    result_head = Solution.removeNthFromEnd(head, n)
    result_list = linkedlist_to_list(result_head)

    assert result_list == expected
