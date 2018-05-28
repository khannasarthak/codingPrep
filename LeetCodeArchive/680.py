class Solution(object):
    def validPalindrome(self, s):
        front = 0 
        last = len(s)-1

        while front<last:
            if s[front]!=s[last]:
                s1 = s[:front]+s[front+1:]
                s2 = s[:last]+s[last+1:]
                # print (s1,s2)
                if s1!=s1[::-1] and s2!=s2[::-1]:
                    return False
                else:
                    return True
            front+=1 
            last-=1 
        return True