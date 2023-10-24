from itertools import *

def prime(n):
    result = []

    for i in range(1, int(n**(1/2))+1):
        if n % i == 0:
            result.append(i)
            if ((i**2) != n) :
                result.append(n//i)
                
    if len(result) == 2:
        return True
    else:
        return False

def solution(nums):
    numlist = list(combinations(nums, 3))
    answer = 0
    
    for num in numlist:
        if prime(sum(num)):
            answer += 1

    return answer