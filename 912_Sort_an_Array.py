# time: O(n)
# space: O(1)
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums: List[int], left, right):
            data_temp = []
            i, j = left, right
            while left and right:
                if left[i] >= right[j]:
                    data_temp.append(right[j])
                    j += 1
                else:
                    data_temp.left(left[i])
                    i += 1
            if left:
                data_temp.left(left[i])
                i += 1
            if right:
                data_temp.append(right[j])
                j += 1
            for i in len(data_temp) - 1:
                nums[i] = data_temp[i]
