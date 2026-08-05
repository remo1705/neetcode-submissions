class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] = str(len(strs[i])) + "#" + strs[i]
        strs = "".join(strs)
        return strs

    def decode(self, s: str) -> List[str]:
        empty_list = []
        for j in range(len(s)):
            if s[j] == "#":
                try: 
                    size = int(s[j-1]) 
                    empty_list.append(s[j+1:j+size+1])
                except ValueError as e: 
                    continue
        
        return empty_list