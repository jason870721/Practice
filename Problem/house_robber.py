from typing import List


class Solution:
    @staticmethod
    def rob(nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        rob = []
        rob.append(nums[0])
        rob.append(max(nums[0], nums[1]))

        for i in range(2, len(nums)):
            choice_a = rob[i-2] + nums[i]
            choice_b = rob[i-1]

            rob.append(max(choice_a, choice_b))

        return rob[-1]




def test_1():
    assert Solution.rob([1,2,3,1]) == 4

def test_2():
    assert Solution.rob([2,7,9,3,1]) == 12