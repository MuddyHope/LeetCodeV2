class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_set = set(words)
        words.sort(key=len)
        
        dp = {}

        for each_word in words:
            dp[each_word] = 1

            # print(f"current_word: {each_word}")

            for i in range(len(each_word)):
                prev = each_word[:i] + each_word[i+1:]
                # print(f"prev : {prev}")
                if prev in word_set:
                    dp[each_word] = max(dp[each_word], dp[prev] + 1)
                # print(f"dp: {dp}")
        max_val = max(dp.values())
        return max_val

        