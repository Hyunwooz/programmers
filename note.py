def solution(my_string, n):
    answer = my_string[-n:]
    return answer

my_string = "ProgrammerS123"
n = 5

print(solution(my_string,n))