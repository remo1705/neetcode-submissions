from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        copy_strs = strs.copy()
        for i in range(len(copy_strs)):
            copy_strs[i] = "".join(sorted(copy_strs[i]))

        for i in range(len(copy_strs)): 
            if copy_strs[i] not in hashmap.keys():
                hashmap[copy_strs[i]].append(strs[i])
            else: 
                hashmap[copy_strs[i]].append(strs[i])
        
        return list(hashmap.values())



            
        