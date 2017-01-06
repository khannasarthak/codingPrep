import collections
class Solution(object):
    def frequencySort(self, s):
        b = collections.Counter(s)
        k = []
        for i in b:
        	k.append(i*b[i])
        k.sort(key=len,reverse=True)
        return ((''.join(k)))
