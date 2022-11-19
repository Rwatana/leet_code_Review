# time: O(n)
# space: O(n)
from typing import List


class Solution:
    
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        both_list = []
        for height, name in zip(heights, names):
            both_list.append([height, name])
            
        namse_in_descending_order_by_height = []
        for data in sorted(both_list, reverse=True):
            namse_in_descending_order_by_height.append(data[1])
            
        return namse_in_descending_order_by_height