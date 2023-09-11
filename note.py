
def solution(x):
    int_sum = 0
    for i in range(0,len(str(x))):
        int_sum += int(str(x)[i])
    
    if x % int_sum == 0:
        answer = True
    else:
        answer = False
        
    return answer

print(solution(12))