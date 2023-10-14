def solution(myString, pat):
    s = myString.replace('A','@').replace('B','A').replace('@','B')
    
    if s.find(pat) != -1:
        answer = 1
    else:
        answer = 0
    return answer

print(solution("ABBAA","AABB"))