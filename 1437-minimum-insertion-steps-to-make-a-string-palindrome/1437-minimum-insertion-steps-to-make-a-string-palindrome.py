class Solution:
    def minInsertions(self, s: str) -> int:
        t = s[::-1]
        n,m = len(s),len(t) #space optimization
        prev = [0] * (m+1)

        for i in range(1,n+1):
            cur = [0] * (m+1)
            for j in range(1,m+1):
                if s[i-1] == t[j-1]:
                    cur[j] = 1 + prev[j-1]
                else:
                    cur[j] = max(prev[j],cur[j-1])
            prev = cur
        lps =  prev[m]
        return n - lps