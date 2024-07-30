class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: # type: ignore
        return len(nums) != len(set(nums))