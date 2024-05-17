class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.defaultdict(int)
        for n in nums:
            counter[n] += 1
        return list(counter.keys())[list(counter.values()).index(max(counter.values()))]