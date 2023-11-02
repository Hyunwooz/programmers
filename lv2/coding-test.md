# Programmers Lv2 코딩테스트 연습문제

## 최댓값과 최솟값

```py
def solution(s):
    str_List = s.split(' ')
    min_str = min(str_List,key=int)
    max_str = max(str_List,key=int)

    answer = min_str+' '+max_str
    return answer
```

## JadenCase 문자열 만들기

```py
def solution(s):
    str_List = list(map(lambda x:x.lower().capitalize(),s.split(' ')))
    return " ".join(str_List)
```

## 올바른 괄호

```py
def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False

    return True
```

## 최솟값 만들기

```py
def solution(A,B):
    answer = 0
    t1 = sorted(A)
    t2 = sorted(B,reverse=True)

    for i in range(len(t1)):
        answer += t1[i] * t2[i]

    return answer
```

## 다음 큰 숫자

```py
def solution(n):
    nxt = n + 1
    while True:
        if str(bin(n)).count('1') == str(bin(nxt)).count('1'):
            break       
        nxt += 1
        
    return nxt
```

## 피보나치 수

```py
def solution(n):
    curr = 0
    next = 1
    for i in range(1,n):
        curr , next = next , curr + next
    return next % 1234567
```

## 짝지어 제거하기

```py
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
```

## 카펫

```py
def solution(brown, yellow):
    block = brown + yellow
    x = int(block ** 0.5)
    
    while True:
        y = block // x
        if x >= y:
            if (x-2)*(y-2) == yellow:
                if x * y == block:
                    break
        x += 1
        
    return [x,y]
```