from itertools import permutations

def solution(user_id, banned_id):
    set_result = []
    result = 0
    for permu in permutations(user_id, len(banned_id)):
        stop = False
        for i in range(len(banned_id)):
            if len(banned_id[i]) != len(permu[i]):
                stop = True
                break
            for j in range(len(banned_id[i])):
                if banned_id[i][j] != "*" and banned_id[i][j] != permu[i][j]:
                    stop = True
                    break
            if stop:
                break
                
        if not stop and set(permu) not in set_result:
            result += 1
            set_result.append(set(permu))
            
    return result