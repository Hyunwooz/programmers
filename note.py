def solution(a, b):
    int_ = [a,b]
    answer = sum(list(range(min(int_),max(int_)+1)))
    return answer

print(solution(2,8))