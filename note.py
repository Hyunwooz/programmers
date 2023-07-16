def solution(s):
    is_p = s.lower().count("p")
    is_y = s.lower().count("s")
    
    if is_p == is_y:
        return True
    elif is_p == 0 and is_y == 0:
        return True
    else:
        return False

my_string = "pPoooyY"

print(solution(my_string))