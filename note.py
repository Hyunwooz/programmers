def solution(sizes):
    side1 = max(max(x) for x in sizes)
    side2 = max(min(x) for x in sizes)
    answer = side1 * side2
    
    return answer


print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))