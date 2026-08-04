class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))
        if len(sorted_s) > len(sorted_t): 
            length = len(sorted_s)
        else: 
            length = len(sorted_t)

        for i in range(1, length): 
            if sorted_t[i] != sorted_s[i]:
                return False
        return True