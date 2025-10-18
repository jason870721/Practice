from typing import List


class Solution:
    @staticmethod
    def containsDuplicate(nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen:
                return True
            seen[num] = True
        return False


def test_1():
    assert Solution.containsDuplicate([1,2,3,1]) == True

def test_2():
    assert Solution.containsDuplicate([1,2,3,4]) == False

def test_3():
    assert Solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True