class Solution(object):
    def wordPattern(self, pattern, str):
        s = {}
        p = {}
        for i in range(len(pattern)):
            # print (pattern[i])
            if pattern[i] in p:
                p[pattern[i]].append(i)
            else:
                p[pattern[i]]=[i]
        for i,word in enumerate((str.split())):

            if word in s:
                s[word].append(i)
            else:
                s[word]=[i]

        return (sorted(s.values())==sorted(p.values()))