from collections import Counter
class Solution(object):
    def judgeCircle(self, moves):
        c = Counter(moves)
        if c['R']==c['L'] and c['U']==c['D']:
            return True
        return False