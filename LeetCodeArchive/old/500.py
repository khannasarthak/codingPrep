class Solution(object):
    def findWords(self, words):
        upper = ['q','w','e','r','t','y','u','i','o','p']
        middle = ['a','s','d','f','g','h','j','k','l']
        lower = ['z','x','c','v','b','n','m']
        upper = upper + list((map(str.upper,upper)))
        middle = middle + list((map(str.upper,middle)))
        lower = lower + list((map(str.upper,lower)))
        words = list(map(str,words))
        out = []
        for i in words:
        	if (set(i).issubset((upper))):
        		out.append(i)
        	elif (set(i).issubset((middle))):
        		out.append(i)
        	elif (set(i).issubset((lower))):
        		out.append(i)
        return out

#Better Solution would be using regex