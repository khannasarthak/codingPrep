class Solution(object):
    def isOneBitCharacter(self, bits):
        i=0
        while i <len(bits)-1:
            i += bits[i]+1
            print (i)
        return ((len(bits)-1)==i)