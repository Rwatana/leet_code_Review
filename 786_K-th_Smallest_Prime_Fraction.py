# T(n**2)
# S(n)
from typing import List


class Solution:

    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        lo, hi = 0, 1.0
        n = len(arr)
        while lo < hi:
            m = (lo+hi) / 2
            maxf, p, q, cnt = 0.0, 0, 0, 0
            j=0
            for i in range(n - 1):
                while j < n and arr[i] / arr[j] > m:
                    j += 1
                cnt += n - j
                if j == n:
                    break

                if arr[i] / arr[j] > maxf:
                    maxf = arr[i] / arr[j]
                    p, q = i, j

            if cnt > k:
                hi = m
            elif cnt < k:
                lo = m
            else:
                return [arr[p], arr[q]]
