class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        
        empty = [0] * len(strs)
        for i in range(len(strs)):
            empty[i] = str(len(strs[i]))

        empty = ",".join(empty) + "#" + ",".join(strs)
        return empty

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        
        copy_s = s
        s = list(s)
        size_list = []
        for i in s: 
            if i == "#":
                start_position = s.index(i)
                break
            elif i == ",":
                continue
            else:
                size_list.append(int(i))
        
        empty_string = ""
        empty_list = []
        for i in size_list: 
            empty_string = copy_s[start_position+1 : start_position + i + 1]
            start_position += i + 1
            empty_list.append(empty_string)
        
        return empty_list