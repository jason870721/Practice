from typing import List


class Solution:
    @staticmethod
    def lengthOfLIS(nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # dp = [1] * len(nums)
        # for i in range(1, len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)

        tails = []
        for i in nums:
            left = 0
            right = len(tails) - 1

            while left <= right:
                mid = (left + right) // 2
                if tails[mid] < i:
                    left = mid + 1
                else:
                    right = mid - 1
            if left == len(tails):
                tails.append(i)
            else:
                tails[left] = i
        return len(tails)




def test_1():
    assert Solution.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4

def test_2():
    assert Solution.lengthOfLIS([0,1,0,3,2,3]) == 4

def test_3():
    assert Solution.lengthOfLIS([7,7,7,7,7,7,7]) == 1