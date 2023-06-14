# lines = [[0, 5], [3, 9], [1, 10]]
lines = [[0, 5], [3, 9], [1, 10]]

def solution(lines):
    l1,l2,l3 = lines
    li = []
    answer = 0
    
    def f(x):
        if len(x) >= 2:
            li.append(x)
    
    a = list(range(l1[0] , l1[1]+1))
    b = list(range(l2[0] , l2[1]+1))
    c = list(range(l3[0] , l3[1]+1))
    
    ab = list(filter(lambda x : x in b, a))
    ac = list(filter(lambda x : x in c, a))
    bc = list(filter(lambda x : x in c, b))
    
    f(ab)
    f(ac)
    f(bc)

    if len(li) == 3:
        sortlist = sorted(set(ab+ac+bc))
        answer += sortlist[-1] - sortlist[0]
    else:
        for i in li:
            answer += i[-1] - i[0]
        
    return answer 

print(solution(lines))

'''
(
    [0, 1], 
    [2, 3, 4, 5], 
    [3, 4, 5, 6, 7, 8, 9])
'''