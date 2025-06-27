class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1: return True
        maxReach = 0

        for i in range(len(nums)):
            if i > maxReach:
                return False
            maxReach = max(maxReach,i+nums[i])
        return True