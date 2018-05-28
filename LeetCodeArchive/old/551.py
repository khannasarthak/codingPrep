class Solution(object):
    def checkRecord(self, s):
        a_count = s.count('A')
        # print (a_count)
        lll_count = s.count('LLL')
        if a_count >1 or lll_count>0:
            return False
        else:
            return True
        """
# Try it with regular expressions as well