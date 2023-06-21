def solution(ingredient):
    answer = 0
    stack=[]
    
    for i in range(len(ingredient)):
        stack.append(ingredient[i])
        if [1,2,3,1] == stack[-4:]:
            answer += 1
            for i in range(4):
                stack.pop()
    return answer