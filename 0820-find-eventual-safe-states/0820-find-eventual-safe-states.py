class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
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
                    