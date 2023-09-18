def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    return sorted(answer)


print(solution([5, 9, 7, 10], 5))
