def solution(s):
    answer = []
    z = 0
    cnt = 0
    
    while s != '1':
        
        z = z + s.count('0')
        
        cnt += 1

s="110010101001"

print(solution(s))