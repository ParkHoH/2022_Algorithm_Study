# 시간 복잡도: O(nm)
def solution(board, moves):
    stack = []
    result = 0
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1]:
                if stack and stack[-1] == board[i][move-1]:
                    stack.pop()
                    result += 2
                else:
                    stack.append(board[i][move-1])
                board[i][move-1] = 0
                break
    return result