class Solution:

    def encode(self, strs: List[str]) -> str:
        length_strs = len(strs)
        empty = ""
        for i in range(length_strs):
            empty = empty + str(len(strs[i])) + "#" + strs[i]
        return empty


    def decode(self, s: str) -> List[str]:
        empty = []
        while s.find("#") != -1:
            position = s.find("#")
            start = s[0:position]
            start = int(start)
            empty.append(s[position+1: position+start+1])
            s = s[position+start+1: len(s)]
            
        return empty