class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ''
        else:
            op =''
            for j,i in enumerate(zip(*strs)):
                
                if len(set(i))==1 and len(op)==j:   #to make sure that only prefix is taken , not the letter that are at end ["aba","cba"]
                    op+=i[0]

            return (op)