class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(city):
            visited[city] = True

            for friend in range(n):
                if isConnected[city][friend] == 1 and not visited[friend]:
                    dfs(friend)
        
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for city in range(n):
            if not visited[city]:
                dfs(city)
                provinces += 1
        return provinces