from collections import Counter
class Solution:
    def judgeCircle(self, moves):
        k = Counter(moves)
        if k['U']==k['D'] and k['R']==k['L']:
            return True
        else:
            return False