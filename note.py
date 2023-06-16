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
        end_day = start_day

        # 0월 0일은 없다.
        
        if start_day[1] + term > 12:
            end_day[1] = (start_day[1] + term) - (12 * ((start_day[1] + term) // 12))
            end_day[0] = end_day[0] + ((start_day[1] + term) // 12)
        else:
            end_day[1] = start_day[1] + term
        
        # end_day와 today의 차이를 구해보자        

    return result

today = "2022.05.19"
terms = ["A 6","B 12","C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]


# 2022.05.19
# 1,3
# 한달은 무조건 28일로
print(solution(today, terms, privacies))