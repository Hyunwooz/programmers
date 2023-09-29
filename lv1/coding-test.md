# Programmers Lv1 코딩테스트 연습문제

## 달리기 경주

```py
def solution(players, callings):

    p_idx = {player : i for i, player in enumerate(players)}
    idx_p = {i : player for i, player in enumerate(players)}

    for i in callings:
        curr = p_idx[i]
        curr_prev = curr-1
        i2 = idx_p[curr_prev]

        idx_p[curr_prev] = i
        idx_p[curr] = i2

        p_idx[i] = curr_prev
        p_idx[i2] = curr

# list로 문제를 풀었을 경우 , 테스트는 통과했지만
# 문제 제출시 시간초과 발생.
# -> dictionary으로 변경 후 진행 성공!
# dictionary는 hash table을 이용함
# hash table은 key값에 따라 value가 저장될 위치가 결정
# 탐색시 key값이 있으면 굳이 배열의 전체를 탐색하지 않고도 value를 얻을 수 있다.
# 이로 인해 list와 dictionary의 탐색속도가 차이가 발생함
```

## 추억 점수

```py
def solution(name, yearning, photo):
    dicts = dict(zip(name,yearning))
    answer = []
    for i in photo:
        point = 0
        for j in i:
            if j in dicts:
                point += dicts[j]
        answer.append(point)
    return answer
```

## 공원 산책

```py
def solution(park, routes):
    space = [list(p) for p in park]

    x, y = 0, 0

    # 시작위치 찾기
    for i in range(len(space)):
        for j in range(len(space[i])):
            if space[i][j] == "S":
                x, y = j, i

    for r in routes:
        op_n = r.split(' ')
        op, n = op_n[0], int(op_n[1])

        is_x = 1
        if op == 'N' and y-n >= 0: # 틀에 벗어나는지 확인
            for i in range(0,n+1): # 중간에 X와 마주치는지 확인
                if space[y-i][x] == 'X':
                    is_x = -1
                    break
            if is_x == 1:
                y -= n
        elif op == 'E' and x+n < len(space[0]) :
            for i in range(0,n+1):
                if space[y][x+i] == 'X':
                    is_x = -1
                    break
            if is_x == 1:
                x += n
        elif op == 'S' and y+n < len(space):
            for i in range(0,n+1):
                if space[y+i][x] == 'X':
                    is_x = -1
                    break
            if is_x == 1:
                y += n
        elif op == 'W' and x-n >= 0:
            for i in range(0,n+1):
                if space[y][x-i] == 'X':
                    is_x = -1
                    break
            if is_x == 1:
                x -= n

    return [y, x]
```

## 바탕화면 정리

```py
def solution(wallpaper):
    x, y = [], []

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                x.append(int(i))
                y.append(int(j))

    lux,luy,rdx,rdy = min(x),min(y),max(x)+1,max(y)+1

    return lux,luy,rdx,rdy
```

## 덧칠하기

```py
def solution(n, m, section):
    answer = 1
    start = section[0]
    for i in range(1, len(section)):
        if section[i] - start >= m:
            answer += 1
            start = section[i]
    return answer
```

## 카드 뭉치

```py
def solution(cards1, cards2, goal):

    for g in goal:
        if cards1 and cards1[0] == g:
            cards1.pop(0)
        elif cards2 and cards2[0] == g:
            cards2.pop(0)
        else:
            return 'No'

    return 'Yes'
```

## 크기가 작은 부분문자열

```py
def solution(t, p):
    answer = 0
    for i in range(len(t)):
        new = t[i:i+len(p)]
        if int(new) <= int(p) and len(new) == len(p):
            answer += 1
    return answer
```

## 푸드 파이트 대회

```py
def solution(food):
    w = ''
    for i in range(len(food)):
        if i > 0:
            w += str(i) * (food[i] // 2)

    return w + "0" + w[::-1]
```

## 명예의 전당(1)

```py
def solution(k, score):

    answer = []
    new_list = []

    for i in score:

        new_list.sort(reverse=True)

        if len(new_list) < k:
            new_list.append(i)
            answer.append(min(new_list))
        else:
            if i > min(new_list):
                new_list.pop()
                new_list.append(i)
            answer.append(min(new_list))

    return answer
```

## 과일 장수

```py
def solution(k, m, score):

    score = list(filter(lambda x : x <= k,score))
    score.sort(reverse=True)
    boxes = len(score) // m

    s, e = 0, m

    answer = 0

    for i in range(0,boxes):
        price = score[s:e]
        answer += min(price) * len(price)
        s = s + m
        e = e + m

    return answer
```

## 자릿수 더하기

```py
def solution(n):
    answer = [int(i) for i in str(n)]

    return sum(answer)
```

## 나머지가 1이 되는 수 찾기

```py
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n % i == 1:
            answer = i
            break
    return answer
```

## x만큼 간격이 있는 n개의 숫자

```py
def solution(x, n):
    return [x+(x*i) for i in range(0,n)]
```

## 햄버거 만들기

```py
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
```

## 약수의 합

```py
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n % i == 0:
            answer += i
    return answer
```

## 문자열 내 p와 y의 개수

```py
def solution(s):
    is_p = s.lower().count("p")
    is_y = s.lower().count("y")
    
    if is_p == is_y:
        return True
    elif is_p == 0 and is_y == 0:
        return True
    else:
        return False
```

## 가장 가까운 같은 글자

```py
def solution(s):
    new_str = []
    answer = []
    for w in s:
        if w in new_str:
            index_ = list(filter(lambda x: new_str[x] == w, range(len(new_str))))
            max_ = max(index_)
            new_str.append(w)
            answer.append(len(new_str) - max_ -1)
        else:
            new_str.append(w)
            answer.append(-1)
            
    return answer
```

## 문자열을 정수로 바꾸기

```py
def solution(s):
    answer = int(s)
    return answer
```

## 정수 내림차순으로 배치하기

```py
def solution(n):
    list_ = list(str(n))
    list_.sort(reverse = True)
    answer = "".join(list_)
    return int(answer)
```

## 서울에서 김서방 찾기

```py
def solution(seoul):
    idx = seoul.index('Kim')
    answer = f'김서방은 {idx}에 있다'
    return answer
```

## 핸드폰 번호 가리기

```py
def solution(phone_number):
    li = list(phone_number)
    
    for i in range(len(phone_number)-4):
        li[i] = '*'
        
    return "".join(li)
```

## 삼총사

```py
from itertools import *

def solution(number):
    answer = 0
    printList = list(combinations(number, 3))
    for li in printList:
        if sum(li) == 0:
            answer += 1
            
    return answer
```

## K번째 수

```py
def solution(array, commands):
    answer = []
    
    for command in commands:
        x,y,z = command
        new_array = array[x-1:y]
        new_array.sort()
        answer.append(new_array[z-1])

    return answer
```

## 예산

```py
def solution(d, budget):
    answer = 0
    n = 0
    d.sort()
    for i in d:
        n += i
        if n > budget:
            break
        answer += 1
    
    return answer
```

## 하샤드 수

```py
def solution(x):
    int_sum = 0
    for i in range(0,len(str(x))):
        int_sum += int(str(x)[i])
    
    if x % int_sum == 0:
        answer = True
    else:
        answer = False
        
    return answer
```

## 2016년

```py
from datetime import datetime

def solution(a, b):
    strToDate = datetime.strptime(f'2016-{a}-{b}', "%Y-%m-%d")
    week = strToDate.weekday()
    
    if week == 0:
        answer = 'MON'
    elif week == 1:
        answer = 'TUE'
    elif week == 2:
        answer = 'WED'
    elif week == 3:
        answer = 'THU'
    elif week == 4:
        answer = 'FRI'
    elif week == 5:
        answer = 'SAT'
    elif week == 6:
        answer = 'SUN'
    
    return answer
```

## 두 정수의 합

```py
def solution(a, b):
    int_ = [a,b]
    return sum(list(range(min(int_),max(int_)+1)))
```

### 콜라츠 추측

```py
def solution(num):
    count = 0
    while num != 1:
        count += 1
        if count > 500:
            count = -1
            break
        
        if num % 2 == 0:
            num = num / 2
        else:
            num = (num * 3) + 1 
    return count
```

### 제일 작은 수 제거하기

```py
def solution(arr):
    arr_min = min(arr)
    idx = arr.index(arr_min)
    arr.pop(idx)
    if len(arr) == 0:
        arr = [-1]
    return arr
```

### 나누어 떨어지는 숫자 배열

```py
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        answer = [-1]
    return sorted(answer)
```

### 없는 숫자 더하기

```py
def solution(numbers):
    answer = 0
    for i in range(0,10):
        if not i in numbers:
            answer += i
    return answer
```

# 음양 더하기

```py
def solution(absolutes, signs):
    answer = 0
    for i in range(0,len(signs)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer
```

# 부족한 금액 계산하기

```py
def solution(price, money, count):
    result = 0
    for i in range(1,count+1):
        result += price * i
    if result - money < 0:
        return 0
    return result - money
```

# 가운데 글자 가져오기

```py
def solution(s):
    if len(s) % 2 == 0:
        s1 = len(s) // 2 - 1
        s2 = len(s) // 2 + 1
        answer = s[s1:s2]
    else:
        answer = s[len(s) // 2]
    
    return answer
```

# 같은 숫자는 싫어

```py
def solution(arr):
    answer = []

    for x,y in enumerate(arr):
        if x == 0:
            answer.append(y)
            continue
        if y != answer[-1]:
            answer.append(y)
            
    return answer
```