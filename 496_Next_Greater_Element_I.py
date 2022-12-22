class Solution:
    
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        dic = {}
        res = []
        
        for num in nums2:
            while stack != [] and num > stack[-1]:
                dic[stack.pop()] = num
            stack.append(num)

        for num in nums1:
            if num in dic.keys():
                res.append(dic[num])
            else:
                res.append(-1)

        return res
