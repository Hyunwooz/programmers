def solution(s):
    
    words = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    
    for n,v in enumerate(words):
        s = s.replace(v,str(n))

    return int(s)

print(solution("23four5six7"))