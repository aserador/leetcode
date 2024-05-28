class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = collections.defaultdict(int)
        for n in nums:
            hashmap[n] += 1
        target = math.floor(len(nums) / 2)
        for n, count in hashmap.items():
            if count > target:
                return n
            
        