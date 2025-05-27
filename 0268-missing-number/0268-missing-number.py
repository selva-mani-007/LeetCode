class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x_or=0

        for i in range(len(nums)):
            x_or^=i^nums[i]

        x_or^=len(nums)
        return x_or