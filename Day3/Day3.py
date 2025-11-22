class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newstring = ""
        for ch in s:
            if ch.isalnum():
                newstring = newstring + ch.lower()
        return newstring == newstring[::-1]
      



        
