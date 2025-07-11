class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps,l,r = 0,0,0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest,i+nums[i])
            l = r+1
            r = farthest
            jumps += 1
        return jumps
"""
jumps = 0
current_end = 0
farthest = 0

for i in range(len(nums) - 1):
    farthest = max(farthest, i + nums[i])
    if i == current_end:
        jumps += 1
        current_end = farthest
"""