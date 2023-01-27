# time: O(n)
# space: O(n)
from collections import deque
from typing import List


class Solution(object):

    def coinChange(self, coins: List[int], amount: int) -> int:

        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        queue = deque([(amount, 0)])
        visited = set()

        while queue:
            amount, count = queue.pop()
            if amount == 0:
                return count

            for coin in coins:
                new_amount = amount - coin
                if new_amount in visited:
                    continue
                if new_amount < 0:
                    continue
                queue.appendleft([new_amount, count + 1])
                visited.add(new_amount)
        return -1
