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
