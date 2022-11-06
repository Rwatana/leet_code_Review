class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        checker = [0] * 26
        for character in sentence:
            checker[ord(character) - ord('a')] += 1
        return 0 not in checker
