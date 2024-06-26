class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        SUM = sum(nums)
        for i in range(len(nums)):
            if left == SUM - nums[i] - left:
                return i
            left += nums[i]
        return -1