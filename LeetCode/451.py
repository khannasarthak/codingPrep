from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        
        c = Counter(s)
        op = []
        st=''   

        op= (sorted(c, key = c.get))[::-1]
        for i in op:
            st+=c[i]*i
        return (st)