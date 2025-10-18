from typing import List
from collections import deque

class Solution:
    @staticmethod
    def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []

        for i, num in enumerate(nums):
            # 過期的刪除
            if q and q[0] <= i-k:
                q.popleft()

            # 小於新的刪除
            while q and nums[q[-1]] < num:
                q.pop()

            #塞入新 index
            q.append(i)

            # 滿足 k 時開始塞入 result
            if i >= k-1:
                result.append(nums[q[0]])

        return result

def test_1():
    assert Solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]

def test_2():
    assert Solution.maxSlidingWindow([1], 1) == [1]

def test_3():
    assert Solution.maxSlidingWindow([1,3,1,2,0,5], 3) == [3,3,2,5]