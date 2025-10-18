from typing import List


class Solution:
    @staticmethod
    def productExceptSelf(nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # 左乘積
        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]

        # 右乘積
        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer


def test_1():
    assert Solution.productExceptSelf([1,2,3,4]) == [24,12,8,6]

def test_2():
    assert Solution.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]

# def test_3():
#     assert Solution.productExceptSelf([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True