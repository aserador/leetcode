class Solution:
    def arraySign(self, nums: List[int]) -> int:
        numNeg = 0
        for num in nums:
            if num < 0:
                numNeg += 1
            elif num == 0:
                return 0
        return 1 if numNeg % 2 == 0 else -1