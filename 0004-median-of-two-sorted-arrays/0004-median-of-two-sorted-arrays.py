class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b = nums1,nums2

        if len(a) > len(b):
            a,b = b,a

        total = len(a) + len(b)
        half = total // 2
        l,r = 0,len(a)

        while l <= r:
            i = (l+r) // 2
            j = half - i

            l1 = a[i - 1] if i > 0 else float("-inf")
            r1 = a[i] if i < len(a) else float("inf")

            l2 = b[j - 1] if j > 0 else float("-inf")
            r2 = b[j] if j < len(b) else float("inf")

            # Partition is good
            if l1 <= r2 and l2 <= r1:
                if total % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return min(r1, r2)
            elif l1 > r2:
                r = i - 1  # Move left in a
            else:
                l = i + 1  # Move right in a
 

