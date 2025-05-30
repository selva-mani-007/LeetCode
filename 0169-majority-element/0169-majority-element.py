class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num,0) + 1
        return max(count_map,key=count_map.get)

    

"""
       res,count=0,0
       for n in nums:
            if count==0:
                res=n

            count+=(1 if n==res else -1)
       return res
"""