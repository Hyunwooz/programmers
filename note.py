def solution(s):
    if len(s) % 2 == 0:
        s1 = len(s) // 2 - 1
        s2 = len(s) // 2 + 1
        answer = s[s1:s2]
    else:
        answer = s[len(s) // 2]
    
    return answer

print(solution("qwer"))