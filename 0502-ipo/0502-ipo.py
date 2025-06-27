class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        projects = list(zip(capital,profits))
        projects.sort()
        i=0
        n = len(projects)
        max_heap = []

        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap,-projects[i][1])
                i+=1
            
            if not max_heap:
                break

            w += -heapq.heappop(max_heap)
        return w
        