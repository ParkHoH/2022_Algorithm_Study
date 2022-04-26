N, M = map(int, input().split())
x, y, direction = map(int, input().split())

left_turn = {
    0: [3, [0, -1]],
    1: [0, [-1, 0]],
    2: [1, [0, 1]],
    3: [2, [1, 0]]
}

back_turn = {
    0: [1, 0],
    1: [0, -1],
    2: [-1, 0],
    3: [0, 1]
}

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

result = 0
cnt = 0
while True:
    if graph[x][y] == 0:
        graph[x][y] = 2
        result += 1

    if cnt == 4:
        dx, dy = back_turn[direction]
        if graph[x+dx][y+dy] == 1:
            break
        else:
            x += dx
            y += dy
            cnt = 0
    else:
        direction, [dx, dy] = left_turn[direction]
        if graph[x+dx][y+dy] == 0:
            x += dx
            y += dy
            cnt = 0
        else:
            cnt += 1

print(result)