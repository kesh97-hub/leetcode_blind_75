from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for num in nums:
            if num - 1 in nums_set:
                continue

            curr = num
            while curr in nums_set:
                curr = curr + 1

            max_len = max(max_len, curr - num)

        return max_len