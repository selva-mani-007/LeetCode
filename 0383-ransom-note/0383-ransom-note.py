class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_count = {}

        for char in magazine:
            letter_count[char] = letter_count.get(char,0) + 1
        
        for char in ransomNote:
            if letter_count.get(char,0) == 0:
                return False
            letter_count[char] -= 1
        return True