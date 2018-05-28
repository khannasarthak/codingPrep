class Solution(object):
    def removeElement(self, nums, val):
        nums[:] = ([x for x in nums if x != val])
        return (len(nums))

# Why nums[:] ->modifies in place, i.e, the previous instances of nums will also et updated with the new values.
# a = [1]; b = a; now a = [2]; b == [1];
# but if [:]  a = [1]; b = a; a[:] = [2]; b == [2], b also gets updated
# https://stackoverflow.com/questions/2186656/how-can-i-remove-all-instances-of-an-element-from-a-list-in-python