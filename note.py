def solution(n):
    arr = list(str(n))
    answer = []
    for i in range(0,len(arr)):
        answer.append(int(arr.pop()))
    return answer

print(solution(12345))
