class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        minLen = min(len(word1), len(word2))
        for i in range(minLen):
            ans += word1[i] + word2[i]
        if minLen == len(word1) == len(word2):
            return ans
        elif minLen == len(word1):
            ans += word2[minLen:]
        else:
            ans += word1[minLen:]
        return ans
        
        