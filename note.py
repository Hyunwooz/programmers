query = [4, 1, 2]
arr = [0, 1, 2, 3, 4, 5]

def solution(arr, query):

    for i in range(len(query)):
        curr = query[i]
        
        if i % 2 == 0:
            arr = arr[:curr+1]
        else:
            arr = arr[curr:]
    return arr

print(solution(arr, query))

