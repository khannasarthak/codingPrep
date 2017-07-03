class Solution(object):
    def isPowerOfThree(self, n):

        if n==0:
            return False
        else:
            while n!=1:
                if n%3==0:
                    n = n//3
                else:
                    return False
                    break
            return (True)

# Another solution without using loops / recursion
    return n > 0 == 3**19 % n
# https://stackoverflow.com/questions/1804311/how-to-check-if-an-integer-is-a-power-of-3/24274850#24274850
# 
# The positive divisors of 3^19 are exactly the powers of 3 from 3^0 to 3^19. 
# That's all powers of 3 in the possible range here (signed 32-bit integer). So just check whether the number is positive and whether it divides 3^19