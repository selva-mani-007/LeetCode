class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = 0

            dirs = [(1,0),(-1,0),(0,1),(0,-1)]

            while q:

                r,c = q.popleft()
                for dr,dc in dirs:
                    nr,nc = r+dr,c+dc

                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        q.append((nr,nc))

        for i in range(n):
            for j in range(m):
                if (i in [0,n-1] or j in [0,m-1]) and grid[i][j] == 1:
                    bfs(i,j)
        
        count = sum(grid[i][j] == 1 for i in range(n) for j in range(m))
        return count