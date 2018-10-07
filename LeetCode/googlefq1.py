# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    
    # h1 S[0] -  0,1,2
    # h2 S[1] - 0-9
    # m1 S[2] - <6
    #  m2 S[3] - 0-9
    
    digits = list(map(int, (''.join(s for s in S if s.isdigit()))))
    minimum = min(digits)
    maximum = max(digits)
    
    # when all numbers same
    if len(set(digits)) == 1:
        return S
    
    op = digits
    
    # CASE 1: m1>m2
    if digits[2]>digits[3]:
        tmp = -1
        for i in digits:
            if i<digits[3]:
                tmp=i
        
        if tmp!=-1:
            op[3] = tmp
        else:
            op[3], op[2] = op[2], op[3]
        
    
    
    # CASE 2: m1<m2
    elif digits[2]<digits[3]:
        
        # op[3] = max less than op[3]
        maxLessThanM2 = 0
        for i in digits[:-1]:
            if maxLessThanM2<digits[3] and maxLessThanM2<i and i<digits[3]:
                maxLessThanM2 = i
        op[3] = maxLessThanM2
        
        
    # CASE 3: m2==m1
    elif digits[2]==digits[3]:
        
        maxLessThan2 = 0
        maxLessThan6 = 0
        
        for i in digits:
            if maxLessThan2<i<=2:
                maxLessThan2 = i
            if maxLessThan6<i<6:
                maxLessThan6=i
        
        op[0] = maxLessThan2
        # op1 = max from op[0] and 0
        op[1] = max(op[0],0)
        op[2] = maxLessThan6
        op[3] = maximum
        
        
    
    return (str(op[0])+str(op[1]) + ':' + str(op[2]) + str(op[3]))
        
        