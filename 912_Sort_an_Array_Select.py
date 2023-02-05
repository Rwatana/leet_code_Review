# time: O(n**2)
# space: O(1)


class Solution(object):
    def sortArray(self, arr):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for ind, ele in enumerate(arr):
            min_ind = min(range(ind, len(arr)), key=arr.__getitem__)
            arr[ind], arr[min_ind] = arr[min_ind], ele
        return arr
