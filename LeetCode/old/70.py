class Solution(object):
    def climbStairs(self, n):
        a=b=1
        for i in range(n):            
            a,b = b , a+b           
            
        return (a)

# Found fibonacci patthern in the number of ways we can climb the stairs.