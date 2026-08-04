class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == [""]:
            return ""
        else:
            empty = "_".join(strs)
        return empty
            

    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]
        else:
            return s.split("_")
