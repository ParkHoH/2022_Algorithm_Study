from collections import deque
from copy import deepcopy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = []

def bfs(x, y, cnt, place):
    queue = deque()
    queue.append((x, y, cnt))
    visited = [[False] * 5 for _ in range(5)]
    visited[x][y] = True
    while queue:
        x, y, cnt = queue.popleft()
        if cnt == 2:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 5 or ny >= 5 or nx < 0 or ny < 0 or place[nx][ny] == "X":
                continue
            if not visited[nx][ny] and place[nx][ny] == "P":
                return False
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, cnt+1))
    return True

def solution(places):
    for place in places:
        stop = False
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P" and not bfs(i, j, 0, place):
                    result.append(0)
                    stop = True
                    break
            if stop: break
        if stop: continue
        result.append(1)
            
    return result