class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course,prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        topo_order = []
        while q:
            node = q.popleft()
            topo_order.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        if len(topo_order) == numCourses:
            return topo_order
        else:
            return []