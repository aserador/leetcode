class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        tracked = set()
        for num in nums:
            if num in tracked:
                return True
            else:
                tracked.add(num)
        return False