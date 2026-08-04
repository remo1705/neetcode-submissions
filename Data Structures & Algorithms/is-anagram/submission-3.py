class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))
        if len(sorted_s) > len(sorted_t): 
            length = len(sorted_s) - 1
        else: 
            length = len(sorted_t) - 1

        for i in range(length): 
            if sorted_t[i] != sorted_s[i]:
                return False
        return True