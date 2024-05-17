class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict() # num : idx
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [i, hashmap[diff]]
            hashmap[n] = i
        return []
