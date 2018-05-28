class Solution(object):
    def searchInsert(self, nums, target):
        if target not in nums:
            if target<nums[0]:
                return (0)
            elif target>nums[-1]:
                return (len(nums))


            for i in range(len(nums)-1):
                if nums[i]<target<nums[i+1]:
                    return (i+1)	
                
        elif target in nums:
	        return (nums.index(target))

           else:
	

            l = 0
            r = len(nums)-1

            while(l<=r):
                mid = (l+r)//2
                if nums[mid]==target:
                    return (mid)
                    
                elif nums[mid]>target:
                    r = mid
                else:
                    l = mid