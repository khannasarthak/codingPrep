class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        op = []
        for i in A:
            i.reverse()
            i = [1-x for x in i]
            op.append(i)
        return (op)
        