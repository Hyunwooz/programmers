# arr = [0, 1, 2, 4, 3]
# queries = [[0, 4, 1],[0, 3, 2],[0, 3, 3]]

# def solution(arr, queries):
#     for s,e,k in queries:
#         for i in range(s,e+1):
#             if i % k == 0:
#                 arr[i] += 1
#     return arr

# # [3, 4, 1, 0, 2]

# print(solution(arr,queries))
# def solution(my_string, m, c):
#     answer = ""
#     s = list(map(''.join, zip(*[iter(my_string)]*m)))
#     print(s)
#     for i in s:
#         answer += i[c-1]
    
#     return answer

# my_string = "ihrhbakrfpndopljhygc"
# m = 4
# c = 2

# print(solution(my_string, m, c))

def solution(my_string, indices):
    indices = sorted(indices)
    s = list(my_string)
    n = 0
    
    for i in indices:
        s.pop(i-n)
        n += 1
        
    return ''.join(s)

my_string = "apporoograpemmemprs"
indices =	[1, 16, 6, 15, 0, 10, 11, 3]

print(solution(my_string, indices))