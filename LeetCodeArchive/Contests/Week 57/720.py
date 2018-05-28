# need to reduce complexity, this is correct but TLE

class Solution(object):
    def longestWord(self, words):
        op = []
        m=0
        f = 0
        for i in (words):
            for j in range(len(i)):
                if (i[:j+1]) not in words:
                    f=0
                    break
                elif (i[:j+1])  in words:
                    f=1 
            if f==1:
                if len(i)>m:
			
                    op.append(i)
        if op:

            return ((max(sorted(op), key=len)))
        else:
            return ('')

# Accepted Solution
# The set contains all the letters 1 by 1 which make a word
class Solution(object):
    def longestWord(self, words):
        words = sorted(words)
        v = set()
        for word in words:
            if len(word)==1 or word[:-1] in v:
                v.add(word)

        return ((max(sorted(v), key=len)))            