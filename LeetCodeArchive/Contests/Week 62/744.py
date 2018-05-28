class Solution(object):
    def nextGreatestLetter(self, letters, target):
        op=''
        if target>=letters[-1]:
            return letters[0]
        for i in letters:
            if i>target:
                return i