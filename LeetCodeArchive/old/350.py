class Solution(object):
    def intersect(self, nums1, nums2):
        a = []
        if not nums1 and not nums2:
            return (nums1)
        else:
            (temp)= (set(nums1).intersection(nums2))
            for i in temp:
                n= (min(nums1.count(i),nums2.count(i)))
                #print (n)
                for j in range(n):
                    a.append(i)
        return a
                
