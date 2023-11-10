def solution(brown, yellow):
    block = brown + yellow
    x = int(block ** 0.5)
    
    while True:
        y = block // x
        if x >= y:
            if (x-2)*(y-2) == yellow:
                if x * y == block:
                    break
        x += 1
        
    return [x,y]


print(solution(18,6))