d = [1,3,2,5,4]
budget = 9

def solution(d, budget):
    answer = 0
    n = 0
    d.sort()
    for i in d:
        n += i
        if n > budget:
            break
        answer += 1
    
    return answer

print(solution(d, budget))