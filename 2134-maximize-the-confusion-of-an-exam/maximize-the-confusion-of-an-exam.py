class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        my_dict = {}
        left, right = 0, 0
        res = 0
        while right < len(answerKey):
            my_dict[answerKey[right]] = 1 + my_dict.get(answerKey[right], 0)
            while (right - left + 1) - max(my_dict.values()) > k:
                my_dict[answerKey[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res