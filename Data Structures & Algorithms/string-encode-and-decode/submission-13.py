class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes = []
        for i in range(len(strs)):
            sizes.append(str(len(strs[i])))
        sizes.append("#")
        
        for i in range(len(strs)):
            sizes.append(strs[i])
        res = ",".join(sizes)
        return res  

    def decode(self, s: str) -> List[str]:
        sizes = []
        res = []
        i = 0
        for i in s: 
            if i == "#": 
                start_position = s.index(i) + 1
                s_part_1 = s[0:s.index(i)-1]
                s_part_2 = s[s.index(i)+1:len(s)].split(",")
        
        for j in s_part_2:
            if j == "":
                s_part_2.pop(s_part_2.index(j))
        return s_part_2