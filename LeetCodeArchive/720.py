class Solution(object):
    def longestWord(self, words):
        wset = set(words)
        op = ''
        for word in words:
            if len(word)>len(op) or len(word)==len(op) and word<op:
                if all(word[:i] in wset for i in range(1,len(word))):
                    op = word
        return (op)