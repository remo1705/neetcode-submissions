class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        for i in sorted_s: 
            if i not in sorted_t: 
                return False
        return True