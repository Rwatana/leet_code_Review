from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        indices = []
        i = 0
        while i < 1:
            sum = numbers[left] + numbers[right]
            if sum == target:
                indices.append(left + 1)
                indices.append(right + 1)
                return indices
            elif sum < target:
                left += 1
            elif sum > target:
                right -= 1
        return 0
    
    class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            new_target= target-numbers[i]
            left , right = i+1, len(numbers)-1
            while left <= right:
                middle = (left+right)//2
                if numbers[middle] > new_target:
                    right = middle-1
                elif numbers[middle] < new_target:
                    left = middle+1
                else:
                    return [i+1,middle+1]
