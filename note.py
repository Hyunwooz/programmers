def solution(n):
    nxt = n + 1
    while True:
        if str(bin(n)).count('1') == str(bin(nxt)).count('1'):
            break       
        nxt += 1
        
    return nxt

print(solution(10))