class Solution:
    def validPalindrome(self, s: str) -> bool:
        count = 0
        p1, p2 = 0, len(s) - 1
        while p2 > p1:
            if s[p1] == s[p2]:
                p1 += 1
                p2 -= 1
            else:
                return self.secondCheck(s, p1 + 1, p2) or self.secondCheck(s, p1, p2 - 1)
        return True

    def secondCheck(self, s: str, p1: int, p2: int) -> bool:
        while p2 > p1:
            if s[p1] == s[p2]:
                p1 += 1
                p2 -= 1
            else:
                return False
        return True
            

                