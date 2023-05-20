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
