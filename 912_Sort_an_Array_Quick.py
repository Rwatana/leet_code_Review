# time: O(nlogn)
# space: O(logn)


class Solution(object):
    def sortArray(self, arr):
        left = []
        right = []
        if len(arr) <= 1:
            return arr

        # データの状態に左右されないためにrandom.choice()を用いることもある。
        # ref = random.choice(arr)
        ref = arr[0]
        ref_count = 0

        for ele in arr:
            if ele < ref:
                left.append(ele)
            elif ele > ref:
                right.append(ele)
            else:
                ref_count += 1
        left = self.sortArray(left)
        right = self.sortArray(right)
        return left + [ref] * ref_count + right
