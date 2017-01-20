import time
start_time = time.time()
###############CODE STARRS##############
import math
    flag = False
        if n>0:
            if n==1:
                flag = True
            while (n>1):
                n=(float(n)/2)
                # print (n)
                if n==1:
                    flag = (True)
                else:
                    flag = (False)
            return (flag)

        else:
            return (False)






###############CODE ENDS################
print("--- %s seconds ---" % (time.time() - start_time))
