class Solution(object):
    def isIsomorphic(self, s, t):
        d1, d2 = {}, {}
        for i in range(len(s)):
            if s[i] in d1:
                d1[s[i]].append(i)
            else:
                d1[s[i]]=[i]
            if t[i] in d2:
                d2[t[i]].append(i)
            else:
                d2[t[i]]=[i]

        return (sorted(d1.values())==sorted(d2.values()))
    