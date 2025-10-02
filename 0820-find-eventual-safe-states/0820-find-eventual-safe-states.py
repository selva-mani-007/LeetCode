class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        
        # Step 1: Reverse the graph
        rev_graph = [[] for _ in range(n)]
        indegree = [0] * n
        
        for u in range(n):
            for v in graph[u]:
                rev_graph[v].append(u)
                indegree[u] += 1
        
        # Step 2: Queue for nodes with indegree 0 (terminal/safe nodes)
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        # Step 3: BFS Topological Sort
        safe = []
        while q:
            node = q.popleft()
            safe.append(node)
            
            for neighbor in rev_graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        # Step 4: Return safe nodes in sorted order
        return sorted(safe)
'''
        N = len(graph)
        vis = [0] * N
        pathvis = [0] * N
        safe = [0] * N

        def dfs(node):
            vis[node] = 1
            pathvis[node] = 1
            for nei in graph[node]:
                if not vis[nei]:
                    if dfs(nei):
                        return True
                elif pathvis[nei]:
                    return True
            
            pathvis[node] = 0
            safe[node] = 1
            return False
        
        for i in range(N):
            if not vis[i]:
                dfs(i)
        
        res = [i for i in range(N) if safe[i] == 1]
        return res
'''
                    