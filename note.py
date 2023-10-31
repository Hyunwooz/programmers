def solution(s):
    
    new_list = []

    for i in s:
        new_list.append(i)
        
        if len(new_list) > 1 and new_list[-1] == new_list[-2]:
            new_list.pop()
            new_list.pop()
    
    if len(new_list) == 0:
        return 1
    else:
        return 0

print(solution('baabaa'))