class Solution(object):
    def reverseWords(self, s):
        a = s.split(" ")
        b = []
        for i in a:
            b.append(str(i[::-1]))
        b = (" ".join(b))  
        return (b)