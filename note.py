import math

def solution(n, m, section):
    answer = 1
    start = section[0]
    for i in range(1, len(section)):
        if section[i] - start >= m:
            answer += 1
            start = section[i]
    return answer

n = 8
m = 4
section = [2,3,6]

print(solution(n,m,section))