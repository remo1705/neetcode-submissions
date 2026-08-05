class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes = []
        for i in range(len(strs)):
            sizes += str(len(strs[i]))
        sizes = ",".join(sizes)
        sizes += "#"
        for i in range(len(strs)):
            sizes += strs[i]
        
        return sizes 

    def decode(self, s: str) -> List[str]:
        sizes = []
        res = []
        i = 0
        for i in s: 
            if i == "#": 
                start_position = s.index(i) + 1
                break
            elif i != ",": 
                sizes.append(i)
            else: 
                continue
        print(sizes)
        
        for i in range(len(sizes)): 
            length = int(sizes[i])
            res.append(s[start_position: start_position+length])
            start_position = start_position + length
        return res