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

## 글자 지우기

```py
def solution(my_string, indices):
    indices = sorted(indices)
    s = list(my_string)
    n = 0

    for i in indices:
        s.pop(i-n)
        n += 1

    return ''.join(s)
```

## 첫 번째로 나오는 음수

```py
def solution(num_list):
    answer = -1
    negative = 0
    for i in num_list:
        answer += 1
        if i < 0:
            negative += 1
            break

    if negative == 0:
        answer = -1

    return answer
```

## 홀수 vs 짝수

```py
def solution(num_list):
    odd = 0
    even = 0
    for n in range(len(num_list)):
        if n % 2 == 0:
            even += num_list[n]
        else:
            odd += num_list[n]

    if odd > even:
        answer = odd
    else:
        answer = even

    return answer
```

## 5명씩

```py
def solution(names):
    answer = []
    for i in range(0 ,len(names), 5):
        answer.append(names[i])
    return answer
```

## 배열의 원소만큼 추가하기

```py
def solution(arr):
    answer = []
    for i in arr:
        for j in range(0,i):
            answer.append(i)
    return answer
```

## 가까운 수

```py
def solution(array, n):
    l = []
    array.sort()
    for i in array:
        l.append(abs(n-i))

    answer = [array[l.index(min(l))]]

    if len(answer) > 1:
        return min(answer)
    else:
        return answer[0]
```

## 간단한 논리 연산

```py
def solution(x1, x2, x3, x4):

    if (x1 or x2) and (x3 or x4):
        answer = True
    else:
        answer = False
    return answer
```

## n 번째 원소까지

```py
def solution(num_list, n):
    answer = []

    for i in range(0,n):
        answer.append(num_list[i])

    return answer
```

## 배열 조각하기

```py
def solution(arr, query):

    for i in range(len(query)):
        curr = query[i]

        if i % 2 == 0:
            arr = arr[:curr+1]
        else:
            arr = arr[curr:]
    return arr
```

## 겹치는 선분의 길이

```py
# 파이써닉한 코드를 위해 고민해야함.
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
```

## 특이한 정렬

```py
def solution(numlist, n):

    numlist.sort(reverse=True)

    answer = sorted(numlist,key=lambda x : abs(n - x))

    return answer
```

## 배열 뒤집기

```py
def solution(num_list):
    answer = num_list[::-1]
    return answer
```

## asd

```py
def solution(my_string, n):
    answer = my_string[-n:]
    return answer
```

## 배열의 평균값

```py
def solution(numbers):
    answer = sum(numbers) / len(numbers)
    return answer
```

## 나이 출력

```py
def solution(age):
    answer = 2023 - age 
    return answer
```

## 양꼬치

```py
import math

def solution(n, k):
    x = math.floor(n/10)
    answer = n * 12000 + k * 2000 - x * 2000
    return answer
```

## 각도기

```py
def solution(angle):
    if 0 < angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif 180 > angle > 90:
        answer = 3
    elif angle == 180:
        answer = 4
    return answer
```

## 편지

```py
def solution(message):
    answer = len(message)*2
    return answer
```

## 최댓값 만들기 (1)

```py
def solution(numbers):
    arr = []
    for i in range(0,2):
        max_ = max(numbers)
        idx = numbers.index(max_)
        rec = numbers.pop(idx)
        arr.append(rec)
        
    return arr[0] * arr[1]
```

## 아이스 아메리카노

```py
def solution(money):
    
    coffee = money // 5500
    changes = money % 5500
    answer = [coffee,changes]
```

## 두수의 곱

```py
def solution(num1, num2):
    answer = num1 * num2
    return answer
```

## 짝수 홀수 개수

```py
def solution(num_list):
    a,b = 0, 0
    for n in num_list:
        if n % 2 == 0:
            a += 1
        else:
            b += 1
    answer = [a,b]
    return answer
```

## 조건에 맞게 수열 변환하기 1

```py
def solution(arr):
    answer = []
    for i in arr:
        if i >= 50:
            if i % 2 == 0:
                answer.append(i/2)
            else:
                answer.append(i)
        else:
            if i % 2 != 0:
                answer.append(i*2)
            else:
                answer.append(i)
    return answer
```

## 소문자로 바꾸기

```py
def solution(myString):
    answer = myString.lower()
    return answer
```

## 3진법 뒤집기

```py
def solution(n):
    answer = ''
    while n >= 1:
        n, rest = divmod(n,3)
        answer += str(rest)
        
    return int(answer,3)
```

## x 사이의 개수

```py
def solution(myString):
    return [len(i) for i in myString.split('x')]
```

## 문자열 바꿔서 찾기

```py
def solution(myString, pat):
    s = myString.replace('A','@').replace('B','A').replace('@','B')
    
    if s.find(pat) != -1:
        answer = 1
    else:
        answer = 0
    return answer
```

## A 강조하기

```py
def solution(myString):
    return myString.lower().replace('a','A')
```