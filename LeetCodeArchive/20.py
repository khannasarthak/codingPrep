class Solution(object):
    
    def isValid(self, s):
        b = {')':'(','}':'{',']':'['}
        stack = []
        for i in s:
            if i in b.values():
                stack.append(i)
            elif i in b.keys():
                if stack==[] or stack.pop()!=b[i]:
                    return False
        return stack==[]