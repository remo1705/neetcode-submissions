class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] = str(len(strs[i])) + "#" + strs[i]
        strs = "".join(strs)
        return strs

    def decode(self, s: str) -> List[str]:
        empty_list = []
    
        for j in range(len(s)):
            size = ""
            if s[j] == "#":
                for k in range(j-1, -1, -1):
                    if s[k].isdigit():
                        size += str(s[k])
                    else:
                        break
                
                if size != "":
                    size = int(size[::-1])
                    empty_list.append(s[j+1:j+size+1])
                
        return empty_list