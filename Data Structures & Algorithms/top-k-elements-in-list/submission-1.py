class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        count = []
        for i in nums:
            if i not in hashmap.keys(): 
                hashmap[i] = 1
            else: 
                hashmap[i] += 1 
                
        for i in list(hashmap.keys()): 
            if hashmap[i] >= k: 
                count.append(i)
        
        return list(dict(sorted(hashmap.items(), key=lambda item: item[1])[::-1]).keys())[0:k]


        