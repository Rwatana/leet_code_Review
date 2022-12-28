# Time: O(n)
# Space: O(1)
from typing import List


class Solution:

    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        lo, hi = 0, 1.0
        arr_length = len(arr)
        while lo < hi:
            mid = (lo+hi) / 2
            maxf, numerator, denominator, cnt = 0.0, 0, 1, 0
            j = 0
            for i in range(arr_length - 1):
                while j < arr_length and arr[i] / arr[j] > mid:
                    j += 1
                cnt += arr_length - j
                if j == arr_length:
                    break

                if arr[i] / arr[j] > maxf:
                    maxf = arr[i] / arr[j]
                    numerator, denominator = arr[i], arr[j]

            if cnt > k:
                hi = mid
            elif cnt < k:
                lo = mid
            else:
                return [numerator, denominator]
