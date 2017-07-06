class Solution(object):
    def lengthOfLastWord(self, s):        
        k = s.split()
        if k==[]:
            return 0           
        else:                
            return (len((k[-1])))
# Read about split()