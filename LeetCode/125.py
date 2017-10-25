class Solution(object):
    def isPalindrome(self, s):
        s = [x.lower() for x in s if x.isalnum()]
        return s==s[::-1]  