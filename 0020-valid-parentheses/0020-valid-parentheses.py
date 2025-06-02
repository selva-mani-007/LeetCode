class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        mapping = {')':'(', '}':'{', ']':'['} 
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if stack == []:
                    return False
                else:
                    if stack.pop() != mapping[c]:
                        return False
        
        return stack == []
        