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
