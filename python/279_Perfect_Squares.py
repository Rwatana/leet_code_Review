# n is the value of input
# time: O(n)
# space: O(n)
from collections import deque
import math


class Solution:

    def numSquares(self, n: int) -> int:
        queue = deque([n])
        depth = 0
        appeared_num = set()
        while queue:
            depth += 1
            width = len(queue)
            for _ in range(width):
                current_num = queue.popleft()
                appeared_num.add(current_num)
                for num in range(1, int(math.sqrt(current_num)) + 1):
                    if current_num - num ** 2 == 0:
                        return depth

                    if not current_num - num ** 2 in appeared_num:
                        queue.append(current_num - num ** 2)

        raise ValueError(f"The input number `{n}` is not a perfect square.")
