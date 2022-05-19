from collections import deque

N = int(input())
graph = []
for _ in range(N):
    graph.append(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

def bfs(x, y, blind):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= N or ny >= N or nx < 0 or ny < 0:
                continue
            
            if not visited[nx][ny] and ((graph[nx][ny] == graph[x][y]) or (blind and (graph[x][y] in ["R", "G"] and graph[nx][ny] in ["R", "G"]))):
                visited[nx][ny] = True
                queue.append((nx, ny))

blind = False
result = []
for k in range(2):
    if k == 1: blind = True
    cnt = 0
    visited = [[False] * (N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                cnt += 1
                bfs(i, j, blind)
    result.append(cnt)

for i in range(2):
    print(result[i], end=" ")