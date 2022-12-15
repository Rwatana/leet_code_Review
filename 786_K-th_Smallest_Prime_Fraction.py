# Time: O(n**2)
# Space: O(n)
from typing import List


class Solution:

    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        lo, hi = 0, 1.0
        arr_length = len(arr)
        while lo < hi:
            mid = (lo+hi) / 2
            maxf, i_1, i_2, cnt = 0.0, 0, 0, 0
            j = 0
            for i in range(arr_length - 1):
                while j < arr_length and arr[i] / arr[j] > mid:
                    j += 1
                cnt += arr_length - j
                if j == arr_length:
                    break

                if arr[i] / arr[j] > maxf:
                    maxf = arr[i] / arr[j]
                    i_1, i_2 = i, j

            if cnt > k:
                hi = mid
            elif cnt < k:
                lo = mid
            else:
                return [arr[i_1], arr[i_2]]
