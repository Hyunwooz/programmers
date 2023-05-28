# import itertools

# def solution(dot):
#     answer = 0
#     nPr = itertools.combinations(dot, 4)
#     a = filter(lambda x: (x[0][1]-x[1][1])*(x[3][0]-x[4][0]) == (x[3][0]-x[2][0])*(x[3][1]-x[2][1]),nPr)
#     if len(list(a)) != 0:
#         answer = 1
        
#     return answer

# #  answer1 = ((y1-y2)*(x3-x4) == (y3-y4)*(x1-x2))
# #     answer2 = ((y1-y3)*(x2-x4) == (y2-y4)*(x1-x3))
# #     answer3 = ((y1-y4)*(x2-x3) == (y2-y3)*(x1-x4))

# from itertools import combinations

# def solution(dots):
#     a = []
#     for (x1,y1),(x2,y2) in combinations(dots,2):
#         a.append((y2-y1,x2-x1))
        
#     for (x1,y1),(x2,y2) in combinations(a,2):
#         if x1*y2==x2*y1:
#             return 1
#     return 0

# print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))

def solution(a, b, c):
    answer = 0
    l = [a,b,c]
    set_l = set(l)
    if len(set_l) == 3:
        answer = (a + b + c)
    elif len(set_l) == 2:
        answer = (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    elif len(set_l) == 1:
        answer = (a + b + c) * (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)
    return answer

a = 2
b = 6
c = 1

print(solution(a, b, c))