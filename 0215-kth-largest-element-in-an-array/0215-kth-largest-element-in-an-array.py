class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        max_heap = [ -num for num in nums ]
        heapq.heapify(max_heap)

        for i in range(k):
            kth_largest = -heapq.heappop(max_heap)
        return kth_largest

'''
        nums.sort()
        while k != 1:
            nums.pop()
            k-=1
        
        return nums.pop()
'''