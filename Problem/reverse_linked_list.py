from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linkedlist(nums: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    for n in nums:
        curr.next = ListNode(n)
        curr = curr.next
    return dummy.next

def linkedlist_to_list(node: Optional[ListNode]) -> list[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

class Solution:
    @staticmethod
    def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous

def test_1():
    head = list_to_linkedlist([1,2,3,4,5])
    reversed_head = Solution.reverseList(head)
    assert linkedlist_to_list(reversed_head) == [5,4,3,2,1]

def test_2():
    head = list_to_linkedlist([1,2])
    reversed_head = Solution.reverseList(head)
    assert linkedlist_to_list(reversed_head) == [2,1]

def test_3():
    head = list_to_linkedlist([])
    reversed_head = Solution.reverseList(head)
    assert linkedlist_to_list(reversed_head) == []

