from collections import defaultdict


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: # type: ignore
        nums = set(nums)
        res = 0

        sequences = defaultdict(int)

        for n in nums:
            consecutiveLeft = sequences[n - 1]
            consecutiveRight = sequences[n + 1]
            consecutive = consecutiveLeft + 1 + consecutiveRight
            res = max(res, consecutive)

            sequences[n - consecutiveLeft] = consecutive   # lower bound of n-1 sequence
            sequences[n + consecutiveRight] = consecutive  # upper bound of n+1 sequence

        return res