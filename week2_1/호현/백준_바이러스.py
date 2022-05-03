import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

queue = deque()
queue.append(1)
visited[1] = True
cnt = 0
while queue:
    n = queue.popleft()
    for node in graph[n]:
        if not visited[node]:
            cnt += 1
            visited[node] = True
            queue.append(node)

print(cnt)