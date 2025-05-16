from typing import List

class Solution:
    def hamming_distance_one(self, s1: str, s2: str) -> bool:
        diff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1

    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [1] * n
        parent = [-1] * n
        longest_sub = 1
        longest_sub_idx = 0

        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]) and self.hamming_distance_one(words[i], words[j]):
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j
                        if dp[i] > longest_sub:
                            longest_sub = dp[i]
                            longest_sub_idx = i

        result = []
        while longest_sub_idx != -1:
            result.append(words[longest_sub_idx])
            longest_sub_idx = parent[longest_sub_idx]

        result.reverse()
        return result
