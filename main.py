def detect_pattern(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    combine = list(zip(s1,s2))
    
    for i in range (len(combine)):
        for j in range(i+1,len(combine)):
            if(combine[i][0] == combine[j][0]):
                return (combine[i][1] == combine[j][1])
            elif(combine[i][1] == combine[j][1]):
                return(combine[i][0] == combine[j][0])

    return True

print(detect_pattern("abb", "aaa"))