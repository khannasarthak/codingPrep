class Solution(object):
    def repeatedStringMatch(self, A, B):        
        if len(B)<len(A):
            k = 1
        else:
            k = len(B)//len(A)
        if B in A*(k):
            return k
        elif B in A*(k+1):
            return k+1
        else:
            return -1