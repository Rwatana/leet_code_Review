from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_num = sorted(nums)
        left , right = 0 , len(nums)-1
        answer_list = []
        while left < right :
            
            sum = n_num[left]+n_num[right]
            if sum == target:
                break
            elif sum > target:
                right -=1
            elif sum < target:
                left +=1

        for i in range( len(nums ) ):
            if nums[i] == n_num[left]:
                answer_list.append(i)
                break
        for i in range( len(nums ) ):
            if nums[i] == n_num[right] and i != answer_list[0]:
                answer_list.append(i)
                break
        return answer_list