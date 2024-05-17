class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Index = {n:i for i, n in enumerate(nums1)}
        ans = [-1] * len(nums1)
        for i in range(len(nums2)):
            if nums2[i] not in nums1Index:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    ans[nums1Index[nums2[i]]] = nums2[j]
                    break
        return ans
        