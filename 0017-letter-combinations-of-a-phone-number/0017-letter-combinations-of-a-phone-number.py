class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        res = []


        digit_to_char = {
            "2": "abc", "3": "def",
            "4": "ghi", "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        def backtrack(index,path):
            if index == len(digits):
                res.append("".join(path))
                return
            
            for letter in digit_to_char[digits[index]]:
                path.append(letter)
                backtrack(index+1,path)
                path.pop()
        
        backtrack(0,[])
        return res
