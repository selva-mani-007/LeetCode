class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = set()
        cur_sum,max_sum,left = 0,0,0

        for right in range(len(nums)):
            
            while nums[right] in seen:
                seen.remove(nums[left])
                cur_sum-=nums[left]
                left+=1
            
            seen.add(nums[right])
            cur_sum+=nums[right]

            if right - left + 1 == k:
                max_sum = max(cur_sum,max_sum)
                seen.remove(nums[left])
                cur_sum-=nums[left]
                left+=1
        
        return max_sum