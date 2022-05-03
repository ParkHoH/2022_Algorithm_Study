from collections import deque

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= N or ny >= N or nx < 0 or ny < 0:
                continue
            
            if graph[nx][ny] == 1:
                cnt += 1
                graph[nx][ny] = 0
                queue.append((nx, ny))

    return cnt

result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            result.append(bfs(i, j))

result.sort()
print(len(result))
for i in result:
    print(i)