class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        n = len(nums)

        def backtrack(i):
            if n == i:
                res.append(sol[:])
                return
            
            # dont pick nums
            backtrack(i+1)

            #pick nums
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)
        return res