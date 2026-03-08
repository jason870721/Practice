from typing import List
import pytest

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                # 情況 A：找到了，回傳目前的索引值
                return mid

            elif nums[mid] < target:
                # 情況 B：目標在右半邊，將左邊界移到 mid 的右邊一格
                left = mid + 1

            else:
                # 情況 C：目標在左半邊，將右邊界移到 mid 的左邊一格
                right = mid - 1

        # 5. 如果整個迴圈結束（left > right）都沒找到，回傳 -1
        return -1


# ---------------------------------------------------------
# 測試區 (注意要拉到與 class 平齊的最外層)
# ---------------------------------------------------------
@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([5], 5, 0),
        ([5], -2, -1),
    ]
)
def test_binary_search(nums, target, expected):
    solver = Solution()
    result = solver.search(nums, target)
    assert result == expected