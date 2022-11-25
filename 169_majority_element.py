# time: O(n)
# space: O(1)
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate_of_majority_element = None
        for num in nums:
            if count == 0:
                candidate_of_majority_element = num
            if num == candidate_of_majority_element:
                count += 1
            else:
                count -= 1
        return candidate_of_majority_element
