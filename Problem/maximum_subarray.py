from typing import List


class Solution:
    @staticmethod
    def maxSubArray( nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            if max_sum < current_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        return max_sum


def test_1():
    assert Solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6

def test_2():
    assert Solution.maxSubArray([1]) == 1

def test_3():
    assert Solution.maxSubArray([5,4,-1,7,8]) == 23