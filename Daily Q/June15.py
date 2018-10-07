# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?
# Google


def q(a,k):
    m = dict()
    
    for i in a:
        print ('M',m)
        if k-i in m:
            return (i,k-i)
        else:
            m[i]=1

print (q([10,15,3,7],10))