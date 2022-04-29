# dfs solution
from copy import deepcopy

def solution(n, info):
    max_arr = [0, []]
    def dfs(i, cnt, score_aphichi, score_lion, board):
        if i > 10:
            board[10] = n - cnt
            if score_lion - score_aphichi > max_arr[0]:
                max_arr[0] = score_lion - score_aphichi
                max_arr[1] = board

            elif max_arr[0] and score_lion - score_aphichi == max_arr[0]:
                change = False
                for i in range(10, -1, -1):
                    if max_arr[1][i] > board[i]:
                        break
                    elif max_arr[1][i] < board[i]:
                        change = True
                        break
                if change:
                    max_arr[1] = board            
                
            return

        required_cnt = info[i] + 1
        if cnt + required_cnt <= n:
            copy_board = deepcopy(board)
            copy_board[i] = required_cnt
            dfs(i+1, cnt+required_cnt, score_aphichi, score_lion+(10-i), copy_board)

        if info[i]:
            copy_board = deepcopy(board)
            dfs(i+1, cnt, score_aphichi+(10-i), score_lion, copy_board)
        else:
            copy_board = deepcopy(board)
            dfs(i+1, cnt, score_aphichi, score_lion, copy_board)

    board = [0] * 11
    dfs(0, 0, 0, 0, board)

    if max_arr[1]:
        return max_arr[1]
    else:
        return [-1]


# combinations solution
from itertools import combinations_with_replacement

def solution(n, info):
    result = [0, []]
    for comb in combinations_with_replacement(range(0, 11), n):
        board = [0] * 11
        for i in comb:
            board[i] += 1
        
        score_aphichi = score_lion = 0
        for i in range(0, 10):
            if board[i] > info[i]:
                score_lion += 10-i
            elif info[i]:
                score_aphichi += 10-i
        
        score_diff = score_lion - score_aphichi
        if score_diff > result[0]:
            result[0] = score_diff
            result[1] = board

        elif result[0] and score_diff == result[0]:
            change = False
            for i in range(10, -1, -1):
                if result[1][i] > board[i]:
                    break
                elif result[1][i] < board[i]:
                    change = True
                    break
            if change:
                result[1] = board
            
    if result[0]:
        return result[1]
    else:
        return [-1]

print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))