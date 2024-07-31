class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: # type: ignore
        output =  [0 for i in range(0, len(nums))]
        # product of numbers to the left of i
        product = 1
        for i in range(0 , len(nums)):
            output[i] = product
            product *= nums[i]
        # * product of numbers to the right of i
        product = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= product
            product *= nums[i]

        return output