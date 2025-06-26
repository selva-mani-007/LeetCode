class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        n = len(nums)
        res = []
        start = nums[0]

        for i in range(1,n):
            if nums[i] != nums[i-1] + 1:
                end = nums[i-1]
                if start == end:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{end}")
                start = nums[i]
        end = nums[-1]
        if start == end:
                res.append(str(start))
        else:
                res.append(f"{start}->{end}")
                 
                
        
        return res