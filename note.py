def solution(s):
    str_List = s.split(' ')
    answer = []
    for i in str_List:
        i.lower()
        i[0] = i[0].upper()
        answer.append(i)
    return answer

s = "3people unFollowed me"

print(solution(s))