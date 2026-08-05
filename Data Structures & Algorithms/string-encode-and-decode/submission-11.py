def encode(strs: list[str]) -> str:
    sizes = []
    for i in range(len(strs)):
        sizes.append(str(len(strs[i])))
    sizes.append("#")
    
    for i in range(len(strs)):
        sizes.append(strs[i])
    res = ",".join(sizes)
    return res 

def decode(s: str) -> list[str]:
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
    
    
print(encode(["we","say",":","yes","!@#$%^&*()"]))
print(decode("2,3,1,3,10,#,we,say,:,yes,!@#$%^&*()"))