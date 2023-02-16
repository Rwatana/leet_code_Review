# time: O(nlogn)
# space: O(n)
from typing import List


class Solution(object):

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        merged = []
        left_index, right_index = 0, 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1
        if left_index < len(left):
            merged.extend(left[left_index:])
        if right_index < len(right):
            merged.extend(right[right_index:])
        return merged

    def divide_and_merge_array(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        left = self.divide_and_merge_array(left)
        right = self.divide_and_merge_array(right)
        return self.merge(left, right)
