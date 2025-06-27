class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open,close,path):
            if open == n and close == n:
                res.append(path)
                return
            if open < n:
                backtrack(open+1,close,path+"(")
            if close < open:
                backtrack(open,close+1,path+")")
        backtrack(0,0,"")
        return res
