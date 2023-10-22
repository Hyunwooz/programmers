def solution(n):
    
    num_list = set(i for i in range(2,n+1)) 
    for i in range(2, int(n ** 1/2) + 1):
        if i in num_list:
            num_list -= set(i for i in range(i*2, n+1,i))
    return len(num_list)

print(solution(10000))