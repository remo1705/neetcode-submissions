class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for i in range(len(sorted(s))):
            if i not in hashmap: 
                hashmap[i] = sorted(s)[i]
            else:
                continue
        
        for j in sorted(t):
            if j not in hashmap.values(): 
                return False
        return True