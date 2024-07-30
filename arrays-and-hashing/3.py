class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: # type: ignore
        targetMap = {}
        res = [0, 0]

        for i in range(0, len(nums)):
            currentSum = target - nums[i]
            if currentSum in targetMap:
                res = [targetMap[currentSum], i]
            else:
                targetMap[nums[i]] = i
        
        return res