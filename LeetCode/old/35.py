class Solution(object):
    def searchInsert(self, nums, target):        
        nums.sort()      
        if target in nums:
	        return ((nums.index(target)))
        else:
            nums.append(target)
            nums.sort()
            return (nums.index(target))

# Maybe improve time complexity 
# Other solution:   return len([x for x in nums if x<target])