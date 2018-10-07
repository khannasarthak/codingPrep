def getNextclosestTime(time):
    digits = list(map(int,(''.join(i for i in time if i.isdigit()))))
    # print (digits)
    sortedDigits = sorted(digits)
    # print (sortedDigits)
    maximum = sortedDigits[-1]
    minimum = sortedDigits[0]
    if len(set(digits))==0:
        return time
    # check if minute 1 >minute 2
    op = digits
    
    if digits[2]>digits[3]:
        print ('Case 1')
        tmp = -1
        for i in digits:
            if i<digits[3]:
                tmp = i
        # print ('tmp', tmp)
        if tmp != -1:
            op[3]= tmp
        else:
            op[3],op[2] = op[2], op[3]
        return (op)
    # check if last digit in bigger than other
    elif digits[2]<digits[3]:
        print ('Case 2', minimum)
        if digits[3]>minimum:
            op[3] = minimum
        return op
    elif digits[2]==digits[3]:
        # digit 0 = 0,1,2
        # digit 2 = 0,1,2,3,4,5
        # max <6
        print ('Case 3')
        maxLessThan6 = 0
        maxLessThan2 = 0

        for i in digits:
            if maxLessThan6<i<6:
                maxLessThan6 = i
            if maxLessThan2<i<=2:
                maxLessThan2= i
            

        if digits[1]>=2:
            op[0] = maxLessThan2
        op[1] = op[0] and minimum        
        op[2] = maxLessThan6
        # print (digits)
        op[3] = maximum         
        
        return op
        
    else:
        print ('Case 4')
        op[2]=op[3]=minimum
        return op



print (getNextclosestTime("22:02"))
