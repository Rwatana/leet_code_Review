class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        matrix = [0] * (n + 1)
        matrix[0] = 1
        matrix[1] = 1

        for i in range(2, n + 1):
            one_digit = int(s[i - 1])
            two_digits = int(s[i - 2:i])

            if one_digit != 0:
                matrix[i] += matrix[i - 1]

            if 10 <= two_digits <= 26:
                matrix[i] += matrix[i - 2]
        return matrix[n]
