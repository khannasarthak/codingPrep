class Solution(object):
    def reverseVowels(self, s):
        
        tmp = list(s)
        vowels = [i for i in range(len(s)) if s[i] in 'aeiouAEIOU']
        for i in range(len(vowels)//2):
            tmp[vowels[i]],tmp[vowels[-i-1]]=tmp[vowels[-i-1]],tmp[vowels[i]]
        return (''.join(tmp))