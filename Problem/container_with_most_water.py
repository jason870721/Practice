from typing import List

class Solution:
    @staticmethod
    def maxArea(height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = 0

        while left < right:
            temp = min(height[left], height[right]) * (right - left)
            area = max(area, temp)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area

def test_1():
    assert Solution.maxArea([1,8,6,2,5,4,8,3,7]) == 49

def test_2():
    assert Solution.maxArea([1,1]) == 1

# def test_3():
#     assert Solution.maxArea([0, 1, 1]) == []