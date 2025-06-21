class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix,suffix = 1,1
        res = float("-inf")
        n = len(nums)

        for i in range(n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

            prefix = prefix * nums[i]
            suffix = suffix * nums[n-i-1]

            res = max(res,prefix,suffix)
        return res