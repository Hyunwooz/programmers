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

## 문제 이름

```py
code
```
