# Time: O(n)
# Space: O(1)
# n = len(students) + len(sandwiches)
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circle_lovers = students.count(0)
        square_lovers = students.count(1)

        for i in range(len(sandwiches)):
            food = sandwiches[i]

            if food == 0:
                if circle_lovers == 0:
                    return square_lovers
                circle_lovers -= 1
            else:
                if square_lovers == 0:
                    return circle_lovers
                square_lovers -= 1
        return 0
