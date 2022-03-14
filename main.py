def detect_pattern(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    combine = list(zip(s1,s2))
    res = True

    for i in range (len(combine)):
        for j in range(i+1,len(combine)):
            if(combine[i][0] == combine[j][0]):
                res = res and (combine[i][1] == combine[j][1])
            elif(combine[i][1] == combine[j][1]):
                res = res and (combine[i][0] == combine[j][0])
    
    return res

print(detect_pattern("aaasssiiii","gggdddfffh"))