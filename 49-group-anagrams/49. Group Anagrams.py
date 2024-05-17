class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letter_groups = collections.defaultdict(list)
        for word in strs:
            letter_groups[tuple(sorted(word))].append(word)
        return letter_groups.values()


