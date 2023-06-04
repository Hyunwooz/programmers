# Programmers Lv0 코딩테스트 연습문제

## 대소문자 바꿔서 출력하기

```python
  str = input()

  def alphaReverse(string):

      new = ""
      for i in string:
          if i.isupper():
              new += i.lower()
          else:
              new += i.upper()
      return new

  new_str = alphaReverse(str)
  print(new_str)
```

## 문자열 섞기

```python

  str1 = "aaaaa"
  str2 = "bbbbb"

  str1_list = list(str1)
  str2_list = list(str2)

  answer = ""

  for i in range(0,len(str1)):
    answer += str1_list[i] + str2_list[i]

  print(answer)

```

## 문자열 겹쳐쓰기

```py
  def solution(my_string, overwrite_string, s):

    str = list(my_string)

    for i in overwrite_string :
        str[s] = i
        s += 1

    answer = "".join(str)

    return answer
```

## 더 크게 합치기

```py
  def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))
```

## 두 수의 연산값 비교하기

```py
def solution(a, b):
    return max(int(f'{a}{b}'),2*a*b)
```

## 홀짝 구분하기

```py

a = int(input())

if a % 2 == 0:
    print(a,"is even")
else:
    print(a,"is odd")

# 3항 연산자로 바꾸기

'is even' if a % 2 == 0 else 'is odd'

```

## 문자열 반복해서 출력하기

```py

a, b = input().strip().split(' ')
b = int(b)
print(a*b)

```

## n의 배수

```py

def solution(num, n):
    if num % n ==0:
        answer = 1
    else:
        answer = 0
    return answer

```

## n의 배수

```py

def solution(num, n):
    if num % n ==0:
        answer = 1
    else:
        answer = 0
    return answer

```

## 공배수

```py

def solution(number, n, m):
    if number % n == 0 and number % m == 0:
        answer = 1
    else:
        answer = 0
    return answer

```

## 홀짝에 따라 다른 값 반환하기

```py

def solution(n):
    if n % 2 == 0:
        return sum([i ** 2 for i in range(2,n+1,2)])
    else:
        return sum([i for i in range(1,n+1,2)])
```

## flag에 따라 다른 값 반환하기

```py
def solution(a, b, flag):
    if flag:
        return a + b
    else:
        return a - b
```

## 조건 문자열

```py
def solution(ineq, eq, n, m):
    if ineq == '<':
        if eq == '=':
            if n <= m:
                return 1
            else:
                return 0
        if eq == '!':
            if n < m:
                return 1
            else:
                return 0
    elif ineq == '>':
        if eq == '=':
            if n >= m:
                return 1
            else:
                return 0
        if eq == '!':
            if n > m:
                return 1
            else:
                return 0
```

## 모음 제거

```py
import re

def solution(my_string):
    return re.sub(r'[aeiou]','',my_string)
```

## 특정 문자 제거하기

```py
import re

def solution(my_string, letter):
    return re.sub(letter,'',my_string)
```

## 숨어있는 숫자의 덧셈 (1)

```py
def solution(my_string):
    return sum([int(i) for i in my_string if i.isdigit()])
```

## 369게임

```py
import re

def solution(order):
    p = re.compile('[369]')
    return len(p.findall(str(order)))
```

## 잘라서 배열로 저장하기

```py
def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0, len(my_str), n)]

# 정규표현식 이용하기
def solution(my_str, n):
    return re.findall(f'.{{1,{n}}}',my_str)

```

## 영어가 싫어요

```py
import re

def solution(numbers):
    s = ''
    d = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
    }
    for i in re.findall(r'(zero|one|two|three|four|five|six|seven|eight|nine)', numbers):
        s += str(d[i])
    return int(s)
```

## 중복된 숫자 개수

```py
def solution(array, n):
    return array.count(n)
```

## 머쓱이보다 키 큰 사람

```py
def solution(array, height):
    return len(list(filter(lambda x:x>height,array)))
```

## 자릿수 더하기

```py
def solution(n):
    answer = sum(list(map(int, str(n))))
    return answer
```

## 숨어있는 숫자의 덧셈(2)

```py
import re

def solution(my_string):
    return sum(map(int,re.findall(r'[\d]+',my_string)))
```

## 옹알이 (1)

```py
import re

def solution(babbling):

    def find_Right_words(text):
        text = re.sub(r'aya|ye|ma|woo','',text)
        if len(text) == 0:
            return True

    answer = 0

    for i in babbling:
        if find_Right_words(i):
            answer += 1

    return answer
```

## qr code

```py
def solution(q, r, code):
    answer = ''
    for i in range(len(code)):
        if i % q == r:
            answer += code[i]
    return answer
```

## 코드 처리하기

```py
def solution(code):
    mode = 0
    ret = ''

    for idx in range(len(code)):
        if mode == 0:
            if code[idx] == '1':
                mode = 1
            elif idx % 2 == 0:
                ret += code[idx]
        elif mode == 1:
            if code[idx] == '1':
                mode = 0
            elif idx % 2 != 0:
                ret += code[idx]

    if ret == '':
        ret = 'EMPTY'

    return ret
```

## 등차수열의 특정한 항만 더하기

```py
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i]:
            answer += a
        a += d
    return answer
```

## 주사위 게임 2

```py
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
```

## 원소들의 곱과 합

```py
def solution(num_list):
    a = 0
    for i in range(len(num_list)):
        if i == 0:
            a = num_list[i]
        else:
            a *= num_list[i]

    if a > sum(num_list) ** 2:
        return 0

    return 1
```

## 이어 붙인 수

```py
def solution(num_list):
    h = ''
    z = ''
    for i in num_list:
        if i % 2 == 0:
            z += str(i)
        else:
            h += str(i)

    return int(h) + int(z)
```

## 마지막 두 원소

```py
def solution(num_list):
    if num_list[-2] >= num_list[-1]:
        num_list.append(num_list[-1] * 2)
    else:
        num_list.append(num_list[-1] - num_list[-2])

    return num_list
```

## 수 조작하기 1

```py
def solution(n, control):
    for i in control:
        if i == 'w':
            n += 1
        elif i == 's':
            n -= 1
        elif i == 'd':
            n += 10
        elif i == 'a':
            n -= 10

    return n
```

## 수 조작하기 2

```py
def solution(numLog):
    result = ''
    for i in range(1,len(numLog)):
        if numLog[i] - numLog[i - 1] == 1:
            result += 'w'
        elif numLog[i] - numLog[i - 1] == -1:
            result += 's'
        elif numLog[i] - numLog[i - 1] == 10:
            result += 'd'
        elif numLog[i] - numLog[i - 1] == -10:
            result += 'a'

    return result
```

## 수열과 구간 쿼리 3

```py
def solution(arr, queries):

    for i,j in queries:
        arr[i] , arr[j] = arr[j] , arr[i]

    return arr
```

## 수열과 구간 쿼리 4

```py
def solution(arr, queries):
    for s,e,k in queries:
        for i in range(s,e+1):
            if i % k == 0:
                arr[i] += 1
    return arr
```

## 카운트 업

```py
def solution(start, end):
    return list(range(start,end+1))
```

## 콜라츠 수열 만들기

```py
def solution(n):
    answer = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            answer.append(n)
        else:
            n = 3 * n + 1
            answer.append(n)

    return answer
```

## 글자 이어 붙여 문자열 만들기

```py
def solution(my_string, index_list):
    answer = ''
    for i in index_list:
        answer += my_string[i]

    return answer
```

## 9로 나눈 나머지

```py
def solution(number):
    answer = int(number) % 9
    return answer
```

## 세로 읽기

```py
def solution(my_string, m, c):
    answer = ""
    s = list(map(''.join, zip(*[iter(my_string)]*m)))

    for i in s:
        answer += i[c-1]

    return answer
```

## 카운트 다운

```py
def solution(start, end):
    answer = []
    while start != end-1:
        answer.append(start)
        start -= 1
    return answer
```

## 문자열의 앞의 n글자

```py
def solution(my_string, n):
    answer = my_string[0:n]

    return answer
```
