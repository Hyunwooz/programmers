def solution(a, b, n):
    answer = 0
    while n >= a:
        t, r = divmod(n,a)
        n = (t * b) + r
        answer += t * b

    return answer

print(solution(3, 1, 25))