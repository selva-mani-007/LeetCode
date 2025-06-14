class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])

        arrows = 1
        arrow_end = points[0][1]

        for start,end in points[1:]:
            if start > arrow_end:
                arrows+=1
                arrow_end = end
        return arrows
