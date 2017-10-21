from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        r = Counter(ransomNote)
        m = Counter(magazine)

        for i in r:
            # print (i,r[i],m[i])
            if i not in m or r[i]>m[i]:
                return False
        return True