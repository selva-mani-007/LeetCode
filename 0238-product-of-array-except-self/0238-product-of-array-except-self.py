class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        result = [1] * n

        for i in range(n):
            result[i] = prefix
            prefix = prefix * nums[i]

        suffix = 1
        for i in range(n-1,-1,-1):
            result[i] = result[i] * suffix
            suffix = suffix * nums[i]

        return result
