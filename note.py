import copy

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
        end_day = copy.deepcopy(start_day)

        if start_day[1] + term > 12:
            end_day[1] = (start_day[1] + term) - (12 * ((start_day[1] + term) // 12))
            end_day[0] = end_day[0] + ((start_day[1] + term) // 12)
        else:
            end_day[1] = start_day[1] + term
        
        to_day_length = (to_day[0] * 12 * 28) + (to_day[1] * 28) + to_day[2]
        end_day_length = (end_day[0] * 12 * 28) + (end_day[1] * 28) + end_day[2]
        
        if end_day_length - to_day_length > 0 :
            result.append(i)
        
    return result

# today = "2022.05.19"
# terms = ["A 6","B 12","C 3"]
# privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]


# 2022.05.19
# 1,3
# 한달은 무조건 28일로
print(solution(today, terms, privacies))