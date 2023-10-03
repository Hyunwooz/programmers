def solution(s):
    strings = s.split(' ')
    new_list = []
    for string in strings:
        result = ''
        for n,v in enumerate(string):
            if n % 2 == 0:
                result += v.upper()
            else:
                result += v.lower()
        new_list.append(result)
    return ' '.join(new_list)

print(solution("try hello wewr world"))