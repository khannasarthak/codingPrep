class Solution:
    def numJewelsInStones(self, J, S):
        op=0
        for i in J:
            op+=S.count(i)

        return (op)