class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows,cols = len(image),len(image[0])
        orig_color = image[sr][sc]

        if orig_color == color:
            return image

        def dfs(r,c):
            image[r][c] = color

            dirs = [(-1,0),(0,1),(1,0),(0,-1)]

            for dr,dc in dirs:
                nr = dr+r
                nc = dc+c

                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == orig_color:
                    dfs(nr,nc)
        
        dfs(sr,sc)
        return image