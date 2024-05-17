class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1set, n2set = set(nums1), set(nums2)
        res1, res2 = set(), set()
        
        for n in n1set:
            if n not in n2set:
                res1.add(n)
        
        for n in n2set:
            if n not in n1set:
                res2.add(n)
            
        return [list(res1), list(res2)]