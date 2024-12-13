# Time Complexity: O(nlogn)
# Space Complexity: O(1)
# n = len(cost)
from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        return self.calculate_minimum_cost(cost)

    def calculate_minimum_cost(self, costs: List[int]) -> int:
        total = 0
        for i, c in enumerate(costs):
            if (i + 1) % 3 != 0:
                total += c
        return total
