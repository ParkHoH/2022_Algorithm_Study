import sys

input = sys.stdin.readline

n, m = map(int, input().split())

r, c, d = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(n)]

clean_yn = [[False] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    # 0이면 3, 1이면  0, 2이면 1, 3이면 2
    global d
    d -= 1
    if d == -1:
        d = 3


count = 1  # 현재 위치 청소
turn = 0  # 회전하는 횟수

while True:
    turn_left()
    nx = r + dx[d]
    ny = c + dy[d]

    if clean_yn[nx][ny] == False and map[nx][ny] == 0:  # 아직 청소하지 않았고, 빈칸일때
        clean_yn[nx][ny] = True
        r = nx
        c = ny
        count += 1
        turn = 0
        continue
    else:
        turn += 1

    if turn == 4:
        nx = r - dx[d]  # 뒤로 이동
        ny = r - dy[d]

        if map[nx][ny] == 0:  # 빈칸일때
            r = nx
            c = ny

        else:
            break
        turn = 0

print(count)
