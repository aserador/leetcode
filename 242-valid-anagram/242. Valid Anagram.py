class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_letters = dict()
        t_letters = dict()

        for l in s:
            if l in s_letters:
                s_letters[l] += 1
            else:
                s_letters[l] = 1
        
        for l in t:
            if l in t_letters:
                t_letters[l] += 1
            else:
                t_letters[l] = 1
        
        return s_letters == t_letters
            
        