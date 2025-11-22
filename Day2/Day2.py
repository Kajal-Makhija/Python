class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        reversed_number = 0
        if(temp < 0):
            return False

        while(temp > 0):
            last_digit = temp%10
            reversed_number = (reversed_number *10) + last_digit
            temp = temp/10
        if reversed_number == x:
            return True
        else: 
            return False
        
