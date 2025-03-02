def solution(bandage, health, attacks):
    b_time, sec_heal, add_heal = bandage
    b_count = 0
    
    now_health = health
    max_health = health
    
    attact_time = attacks[-1][0]
    
    
    attack_dict = {}
    
    for attack in attacks:
        attack_dict[attack[0]] = attack
    
    for i in range(1, attact_time + 1):
        try:
            now_health = now_health - attack_dict[i][1]
            b_count = 0
            if now_health <= 0:
                now_health = -1
                
                break
        except:
            b_count = b_count + 1
             
            if now_health + sec_heal >= max_health:
                now_health = max_health
            else:
                if b_count == b_time:
                    now_health = now_health + sec_heal + add_heal
                    
                    if now_health + sec_heal + add_heal >= max_health:
                        now_health = max_health
                    b_count = 0
                else:
                    now_health = now_health + sec_heal

    return now_health

solution([5, 1, 5],30,[[2, 10], [9, 15], [10, 5], [11, 5]])