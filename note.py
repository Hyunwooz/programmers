# user_input = int(input())

# def solution(n):
#   if n % 2 == 0:
#     return sum([i ** 2 for i in range(2,n+1,2)])
      
#   else:
#     return sum([i for i in range(1,n+1,2)])

# print(solution(user_input))

# players = ["mumu", "soe", "poe", "kai", "mine"]
# callings = ["kai", "kai", "mine", "mine"]

# def solution(players, callings):
#     p_idx = {player : i for i, player in enumerate(players)}
#     idx_p = {i : player for i, player in enumerate(players)}
  
#     for i in callings:
#         curr = p_idx[i] # 현재 등수
#         curr_prev = curr-1 # 앞 사람 등수
#         i2 = idx_p[curr_prev] # 앞 사람 이름
        
#         idx_p[curr_prev] = i 
#         idx_p[curr] = i2
        
#         p_idx[i] = curr_prev
#         p_idx[i2] = curr
#     return list(idx_p.values())

# print(solution(players,callings))

#result = ["mumu", "kai", "mine", "soe", "poe"]


def solution(name, yearning, photo):
    dicts = dict(zip(name,yearning))
    answer = []
    for i in photo:
        point = 0
        for j in i:
            if j in dicts:
                point += dicts[j]
        answer.append(point)
    return answer

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo =[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

# [19, 15, 6]
print(solution(name,yearning,photo))