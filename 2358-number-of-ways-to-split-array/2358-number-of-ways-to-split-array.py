class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count = 0
        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)-1):
            left_sum = left_sum + nums[i]
            right_sum = total_sum -left_sum

            if left_sum >= right_sum:
                count+=1
        return  count


