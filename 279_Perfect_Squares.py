# time: O(n**2)
# space: O(n)


class Solution(object):

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        powers = set([i*i for i in range(int(n**0.5)+1)])

        def search_possibility(nums):
            if powers & nums:
                return 1
            newnums = set()
            newnums.update({num - p for num in nums for p in powers if num - p >= 0})
            return search_possibility(newnums) + 1

        return search_possibility(set([n]))
