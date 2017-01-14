word = s
        count = {}
        b = []
        for c in word:
        	if c not in count:
        		count[c] = 0
        	count[c] +=1
        for c in word:
        	if count[c]==1:
        		# print (word.index(c))
        		b.append(c)
        if not b:
        	return (-1)
        else:
        	return (word.index(b[0]))
