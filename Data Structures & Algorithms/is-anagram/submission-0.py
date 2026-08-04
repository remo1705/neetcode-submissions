class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))
        for i in range(len(sorted_s)): 
            if sorted_t[i] != sorted_s[i]:
                return False
        return True