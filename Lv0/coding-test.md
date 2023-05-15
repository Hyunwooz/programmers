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
