class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: 
            return ""
        else:
            empty = ",".join(strs)
        return empty
            

    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]
        else:
            return s.split(',')
