#O(n) T(nlogn)
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
          
        def mergeSort(self, nums: List[int]) -> List[int]:
            if not nums:
                return nums
            if len(nums) == 1:
                return nums
            mid = len(nums) // 2
            left_nums = nums[:mid]
            right_nums = nums[mid:]
            return self.merge(self.mergeSort(left_nums), self.mergeSort(right_nums))
        
        def merge(self, left_nums: List[int], right_nums: List[int]) -> List[int]:
            
            i = 0
            j = 0
            final_arr = []
            while i < len(left_nums) and j < len(right_nums):
                if left_nums[i] <= right_nums[j]:
                    final_arr.append(left_nums[i])
                    i += 1
                else:
                    final_arr.append(right_nums[j])
                    j += 1
            while i < len(left_nums):
                final_arr.append(left_nums[i])
                i += 1
            while j < len(right_nums):
                final_arr.append(right_nums[j])
                j += 1
            return final_arr
