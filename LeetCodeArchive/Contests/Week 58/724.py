k = sum(nums)
        lsum=0
        rsum=0
        for i in range(len(nums)):

            k -= nums[i]
            # print (k,lsum)
            if lsum==k:
                return i 
            lsum+=nums[i]

        return -1