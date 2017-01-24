import time
start_time = time.time()
###############CODE STARRS##############
n = -1
val = ''

if n==0:
    print (0)
elif n>0:
    while (n>0):
        # print (n)
        a = (n%16) # check for hex conversion
        if a<=9:
            val += str(a)
        elif a>9 and a<=15:
            # print ('asdfasdf-',str(chr(55+a)))
            val+= str(chr(55+a))
        n = int(n/16)
    print (val[::-1])
elif n<0:       # implement -ve
    b = -(n) # -ve of n
    while (b>0):
        newa = b%2
        val += str(newa)
        b =int(b/2)
    val = val[::-1]

    if len(val)%8!=0:
        (buffval) = val[::-1]
        for i in range(8-(len(val)%8)):
            buffval+='0'
        finalval = buffval[::-1]
    else:
        finalval = val



print (len(val))
print (hex(int(finalval)))




###############CODE ENDS################
print("--- %s seconds ---" % (time.time() - start_time))
