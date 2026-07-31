class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {}
        hashmap_t = {}
        for i in s: 
            if i not in hashmap_s.keys(): 
                hashmap_s[i] = 1
            else:
                hashmap_s[i] += 1
                
        for j in t: 
            if j not in hashmap_t.keys():
                hashmap_t[j] = 1 
            else:
                hashmap_t[j] += 1

        return hashmap_s == hashmap_t

        