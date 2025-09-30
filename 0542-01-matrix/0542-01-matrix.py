class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n,m = len(mat),len(mat[0])

        vis = [[0 for _ in range(m)] for _ in range(n)]
        dist = [[0 for _ in range(m)] for _ in range(n)]

        q = deque()

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i,j,0))
                    vis[i][j] = 1
        
        delRow = [-1,0,1,0]
        delCol = [0,1,0,-1]

        while q:
            row,col,steps = q.popleft()
            dist[row][col] = steps

            for i in range(4):
                nrow = row + delRow[i]
                ncol = col + delCol[i]

                if 0 <= nrow < n and 0 <= ncol < m and not vis[nrow][ncol]:
                    q.append((nrow,ncol,steps+1))
                    vis[nrow][ncol] = 1
        
        return dist

