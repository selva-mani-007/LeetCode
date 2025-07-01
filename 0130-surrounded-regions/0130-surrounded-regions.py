class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows,cols = len(board),len(board[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols :
                return 
            if visited[r][c] == 1 or board[r][c] != 'O':
                return
            visited[r][c] = 1

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(rows):
            if board[r][0] == 'O' and visited[r][0] == 0:
                dfs(r,0)
            if board[r][cols-1] == 'O' and visited[r][cols-1] == 0:
                dfs(r,cols-1)
        
        for c in range(cols):
            if board[0][c] == 'O' and visited[0][c] == 0:
                dfs(0, c)  # \U0001f539 First row
            if board[rows-1][c] == 'O' and visited[rows-1][c] == 0:
                dfs(rows-1, c)  # \U0001f539 Last row

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and visited[r][c] == 0:
                    board[r][c] = 'X'