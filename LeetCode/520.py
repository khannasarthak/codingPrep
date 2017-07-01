class Solution(object):
    def detectCapitalUse(self, word):
        # if (word.isupper() or word.islower()):
        #     return (True)
        # elif (word[0].isupper() and word[1:].islower()):
        #     return (True)
        # else:
        #     return (False)
        return word.isupper() or word.islower() or word.istitle()