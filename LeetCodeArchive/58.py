class Solution(object):
    def lengthOfLastWord(self, s):
        
        k = s.split()
        if k==[]:
            return 0
        return len(k[-1])