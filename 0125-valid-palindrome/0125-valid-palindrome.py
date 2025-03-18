class Solution:
    def isPalindrome(self, s: str) -> bool:

        filtered =''.join(char.lower() for char in s if char.isalnum())

        return filtered == filtered[::-1]
  
'''  
        if s==" ":
            return True
        demo='QWERTYUIOPASDFGHJKLZXCVBNM' + 'qwertyuiopasdfghjklzxcvbnm' + '1234567890'
        strl=''
        for i in s:
            if i in demo:
                strl+=i

        if strl.upper()==strl[::-1].upper() or strl.upper()==strl[-1].upper():
            return True
        else:
            return False
'''
