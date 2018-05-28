class Solution(object):
    def findWords(self, words):
        r1 = 'qwertyuiop'
        r2 = 'asdfghjkl'
        r3 = 'zxcvbnm'

        op = []

        for i in words:
            if not (set(i.lower()) - set(r2)) or not (set(i.lower()) - set(r1)) or not (set(i.lower()) - set(r3)):
                op.append(i)
        return (op)