# time: O(n**2)
# space: O(1)


class Solution(object):
    def sortArray_bubbleSort(self, arr):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        change = True
        while change:
            change = False
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    change = True
        return arr
