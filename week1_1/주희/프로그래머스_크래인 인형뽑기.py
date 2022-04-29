### 문제 요약
# 인형이 아래에서 부터 쌓여있는 크레인판에서 인형을 바구니로 옮기려고 한다.
# 같은 두개의 인형이 쌓이면 같은 인형들을 없어진다.
# 터트려져 사라지는 인형의 개수를 구하여라.

### 입력
# 1. 게임 화면의 격자 상태가 담긴 2차원 배열 board (5*5 이상 30*30 이하, 0은 빈칸을 의미, 각 칸은 1~100사이의 숫자)
# 2. 크레인을 작동시킨 위치가 담긴 배열 moves (1 이상 1000이하, 배열 안의 값은 1이상 가로크기 이하 자연수)

### 출력
# 1. 크레인을 모두 작동시킨 후 터트러져 사라진 인형의 개수

### 아이디어
# 1. moves 와 board를 이중 for문으로 돌려서 각 값의 -1한 값들을 board의 인덱스로 가져오기
# 3. 바구니 크기가 0이 아닐경우, 그 전 인덱스와 비교해서 같은 값이면 count 를 +1해주기.

### 시간 복잡도
# 1. moves 크기 * board 의 배열 하나의 크기
# 2. 30 * 30 -> 900

### 자료구조
# 1. board : int[][]
# 2. moves : int[]
# 3. result(바구니) : int[]
# 4. answer : 0

def solution(board, moves):
    result = []
    answer = 0

    for index in moves:
        for grid in board:
            if grid[index - 1] != 0:  # 인형이 있으면
                result.append(grid[index - 1])  # 바구니에 담아주기

                if len(result) > 1:  # 바구니에 인형이 2개 이상 있을때
                    if result[-2] == result[-1]:
                        del result[-2]
                        del result[-1]
                        answer += 2

                grid[index - 1] = 0  # 이미 뽑았기 때문에 0으로 변경
                break
    return answer