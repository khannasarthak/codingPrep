class Solution(object):
    def anagramMappings(self, A, B):
        op = []

        for i in A:
            op.append(B.index(i))
        return op