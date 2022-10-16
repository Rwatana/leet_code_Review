from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            for j in range(i+1,len(arr),1):
                if arr[i] <0 and arr[j] < 0:
                    i_abs = abs(arr[i])
                    j_abs = abs(arr[j])
                    if j_abs*2 == i_abs:
                        return True
                if arr[i]*2 == arr[j]:
                        return True

        return False