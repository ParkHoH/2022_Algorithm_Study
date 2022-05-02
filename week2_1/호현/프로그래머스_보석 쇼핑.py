from collections import defaultdict

def solution(gems):
    dic = defaultdict(int)
    min_len = float('inf')
    len_gems = len(set(gems))
    result = [0, 0]
    start = end = 0
    while start < len(gems):
        if len(dic) == len_gems and end - start < min_len:
            min_len = end - start
            result = [start+1, end]

        if dic[gems[start]] >= 2:
            dic[gems[start]] -= 1
            start += 1
        else:
            if end == len(gems):
                break
            dic[gems[end]] += 1
            end += 1
            
    return result