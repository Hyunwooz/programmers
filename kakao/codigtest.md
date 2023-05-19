## 2018 KAKAO BLIND RECRUITMENT

### 1차 캐시문제 LV2

```py
from collections import deque

def solution(casheSize, cities):
    l = [''] * casheSize
    cache = deque(l,maxlen=casheSize) # 길이 제한
    answer = 0
    for city in cities:
        city = city.lower() # 소문자 변환
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else: # cache miss
            answer += 5
            cache.append(city)
    return answer
```
