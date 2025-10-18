from typing import List

class Solution:
    @staticmethod
    def threeSum(nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left_pointer = i + 1
            right_pointer = len(nums) - 1
            while left_pointer < right_pointer:
                total = nums[i] + nums[left_pointer] + nums[right_pointer]

                if total == 0:
                    answer.append([nums[i], nums[left_pointer], nums[right_pointer]])

                    left_pointer += 1
                    right_pointer -= 1
                    while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer - 1]:
                        left_pointer += 1
                    while left_pointer < right_pointer and nums[right_pointer] == nums[right_pointer + 1]:
                        right_pointer -= 1
                elif total < 0:
                    left_pointer += 1
                else:
                    right_pointer -= 1
        return answer

def test_1():
    assert Solution.threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]

def test_2():
    assert Solution.threeSum([0,1,1]) == []

def test_3():
    assert Solution.threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]) == [[-10,5,5],[-5,0,5],[-4,2,2],[-3,-2,5],[-3,1,2],[-2,0,2]]