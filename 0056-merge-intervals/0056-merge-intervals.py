class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x : x[0])
        output = []
        output.append(intervals[0])

        for start,end in intervals[1:]:
            lastEnd = output[-1][1]

            if lastEnd >= start:
                output[-1][1] = max(end,lastEnd)
            else:
                output.append([start,end])

        return output