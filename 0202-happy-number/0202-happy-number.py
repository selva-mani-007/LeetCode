class Solution:
    def isHappy(self, n: int) -> bool:
       seen=set()

       while n!=1 and n not in seen:
            seen.add(n)
            r=0
            while n>0:
                r+=(n%10)**2
                n//=10
            n=r
       return n==1