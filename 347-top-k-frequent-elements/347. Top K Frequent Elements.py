class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        hashmap = collections.defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]
        ans = []

        for num in nums:
            hashmap[num] += 1
        
        for num, count in hashmap.items():
            freq[count].append(num)
        
        kcount = 0
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                if(kcount == k):
                    return ans
                ans.append(num)
                kcount += 1
        return ans


        
        