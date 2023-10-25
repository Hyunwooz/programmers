def solution(arr1, arr2):
    answer = []
    for a,b in zip(arr1,arr2):
        arr = []
        for i, j in zip(a,b):
            arr.append(i+j)
        answer.append(arr)
    return answer

print(solution([[1,2],[2,3]],[[3,4],[5,6]]))