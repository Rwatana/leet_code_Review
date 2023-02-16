# time: O(nlogn)
# space: O(logn)
from typing import List


class Solution(object):
    
    def sortArray(self, arr: List[int]) -> List[int]:
        left = []
        right = []
        if len(arr) <= 1:
            return arr

        comparision_number = arr[0]
        count_comparision_number = 0

        for each_num in arr:
            if each_num < comparision_number:
                left.append(each_num)
            elif each_num > comparision_number:
                right.append(each_num)
            else:
                count_comparision_number += 1
        left = self.sortArray(left)
        right = self.sortArray(right)
        return left + [comparision_number] * count_comparision_number + right
