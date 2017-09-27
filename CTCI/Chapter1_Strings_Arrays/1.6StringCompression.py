s = 'abcdddddd'

s=s.lower()
# print (len(s))
c = 0

op = ''
for i in range(0,len(s)-1):
	
	# print (i,s[i],s[i+1])
	c +=1
	
	if s[i]!=s[i+1] or i+1==len(s)-1:
		
		# 	op += s[i]+str(c+1)
		# 	print ('asfd')
		# 	c=0
		# else:
		op += s[i]+str(c)
		# print (c)
		c=0

op = list(op)
op[-1] = str(int(op[-1])+1)
op = ''.join(op)
print (len(op),len(s))

if len(op)<len(s):
	# print ('sdfgsdg)')
	print (op)
else:
	print (s)
