nums.sort()
c = 0
for i in range(1,len(nums)+1,2):
	print (i)
	# op.append(min(nums[i],nums[i+1]))
	c += (min(nums[i],nums[i-1]))

print (c)



