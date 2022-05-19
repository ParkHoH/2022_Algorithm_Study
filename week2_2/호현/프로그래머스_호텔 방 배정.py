def solution(k, room_number):
    dic = {}
    result = []
    for num in room_number:
        if num in dic:
            temp = []
            idx = dic[num]
            while True:
                if idx in dic:
                    idx = dic[idx]
                    temp.append(idx)
                else:
                    result.append(idx)
                    temp.append(idx)
                    for ele in temp:
                        dic[ele] = idx + 1
                    break
        else:
            result.append(num)
            dic[num] = num + 1
            
    return result