def solution(phone_number):
    
    li = list(phone_number)
    
    for i in range(len(phone_number)-4):
        li[i] = '*'
    return "".join(li)

print(solution("01033334444"))