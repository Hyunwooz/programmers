def solution(numlist, n):
    numlist.sort(reverse=True)
    answer = sorted(numlist,key=lambda x : abs(n - x))
    return answer

numlist = [10000,20,36,47,40,6,10,7000]
n = 30

print(solution(numlist, n))

# [36, 40, 20, 47, 10, 6, 7000, 10000]