def solution(n, k, cmd):
    linked = {i: [i-1, i+1] for i in range(n)}
    linked[0], linked[n-1] = [None, 1], [n-2, None]
    eliminated_list = []
    result = ["O"] * n
    for command in cmd:
        if command[0] == "D" or command[0] == "U": # 커서 이동
            direction, num = command.split()
            if direction == "D":
                for _ in range(int(num)):
                    k = linked[k][1]
            else:
                for _ in range(int(num)):
                    k = linked[k][0]
            
        elif command == "C": # 삭제
            result[k] = "X"
            prev, after = linked[k]
            eliminated_list.append([k, prev, after])
            k = prev if after == None else after
            if prev == None:
                linked[after][0] = prev
            elif after == None:
                linked[prev][1] = after
            else:
                linked[prev][1] = after
                linked[after][0] = prev
        
        else: # 되돌리기
            idx, prev, after = eliminated_list.pop()
            result[idx] = "O"
            if prev and after:
                linked[prev][1] = idx
                linked[after][0] = idx
            elif prev:
                linked[prev][1] = idx
            elif after:
                linked[after][0] = idx
                
    return ''.join(result)