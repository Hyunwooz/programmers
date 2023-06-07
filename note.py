def solution(food):
    w = ''
    for i in range(len(food)):
        if i > 0:
            w += str(i) * (food[i] // 2)
            
    return w + "0" + w[::-1]