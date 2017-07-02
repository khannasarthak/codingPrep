class Solution(object):
    def isUgly(self, num):
        ugly = [2,3,5]
        factors = []
        if num<=0:
            return (False)

        elif num==1:
            return (True)

        else:
            #print ('test')
            d = 2
            while num>1:
                while num%d==0:
                    factors.append(int(d))
                    num = num/d
                d = d+1
                if d*d>num:         #makes the check faster, no need to go upto n
                    if num>1:
                        factors.append(num)
                        break
                
       # print (factors)
        for i in ugly:
             factors=(list(filter(lambda a: a != i, factors)))
        #print (factors)
        if (len(factors)!=0):
            return (False)
        else:
            return (True)

# Better solution, divide number by 2,3,5 as many times as possible and check if you arrive at 1, if yes then ugly , otherwise not ugly

    # if num <= 0:
    #     return False
    # for x in [2, 3, 5]:
    #     while num % x == 0:
    #         num = num / x
    # return num == 1