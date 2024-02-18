from itertools import *

def solution(list):
    answer = [(a+b) for a,b in combinations(list, 2)]   
    return sorted([*set(answer)])

print(solution([2,1,3,4,1,7]))