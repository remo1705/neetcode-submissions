class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}
        output = 0
        if nums == []:
            return output
        else: 
            for i in nums:
                hashmap[i] = i+1
            print(hashmap.values())
            for i in hashmap.values(): 
                if i in hashmap.keys():
                    output += 1
        
        return (output+1)