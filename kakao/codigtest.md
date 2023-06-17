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

## 2023 KAKAO BLIND RECRUITMENT 

### 개인정보 수집 유효기간

```py
def solution(today, terms, privacies):

    split_terms = list(map(lambda x:x.split(" "),terms))
    split_privacies = list(map(lambda x:x.split(" "),privacies))

    terms = {a:b for a,b in split_terms}
    privacies = {idx:{"day":d,"terms":t} for idx,[d,t] in enumerate(split_privacies)}
    
    result = []
    
    for i in range(len(privacies)):
        privacy = privacies[i]
        term = int(terms[privacy["terms"]])
        
        to_day = list(map(int,today.split(".")))
        start_day = list(map(int,privacy["day"].split(".")))
        end_day = list(map(int,privacy["day"].split(".")))
                
        if start_day[1] + term >= 13:
            end_day[1] = (start_day[1] + term) - (12 * ((start_day[1] + term) // 12))
            end_day[0] = end_day[0] + ((start_day[1] + term) // 12)
        else:
            end_day[1] = start_day[1] + term
        
        to_day_length = (to_day[0] * 12 * 28) + ((to_day[1] - 1) * 28) + to_day[2]
        end_day_length = (end_day[0] * 12 * 28) + ((end_day[1] - 1) * 28) + end_day[2]
                
        if to_day_length - end_day_length >= 0 :
            result.append(i + 1)

    return result
```