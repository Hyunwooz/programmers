def solution(survey, choices):
    answer = ''
    
    types = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    
    score = [3,2,1,0,1,2,3]
    
    for i in range(len(survey)):

        if choices[i] == 4:
            continue
        elif choices[i] <= 3:
            
            plus_score = score[choices[i]-1]
            plus_type = survey[i][0]
            types[plus_type] = types[plus_type] + plus_score
            
        elif choices[i] >= 5:
            
            plus_score = score[choices[i]-1]
            plus_type = survey[i][1]
            types[plus_type] = types[plus_type] + plus_score

        
    return types

survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]

print(solution(survey, choices))


# 지표 번호	성격 유형
# 1번 라이언형(R), 튜브형(T)
# 2번 콘형(C), 프로도형(F)
# 3번 제이지형(J), 무지형(M)
# 4번 어피치형(A), 네오형(N)
# "RCJA"