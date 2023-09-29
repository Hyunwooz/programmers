def solution(arr):
    answer = []

    for x,y in enumerate(arr):
        if x == 0:
            answer.append(y)
            continue
        if y != answer[-1]:
            answer.append(y)
            
    return answer

print(solution([1,1,3,3,0,1,1]))