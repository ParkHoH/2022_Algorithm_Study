### 문제
# 크기가 n*n 인 도시가 있다.
# 각 칸은 빈칸, 치킨집, 집 중 하나이다. (0은 빈칸, 1은 집, 2는 치킨집)
# 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이고, 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.
# 거리는 |r1-r2| + |c1-c2|로 구한다.
# 도시에 있는 치킨집 중에서 최대 M개를 고를 때, 어떻게 고르면 도시의 치킨 거리가 가장 작게 될지 구하라.

### 입력
# 첫째 줄 : N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)
# 둘째 줄 ~ N개의 줄 : 도시의 정보 (집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재한다.)

### 출력
# 첫째 줄에 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값

### 아이디어
# 모든 2에 대해 도시의 치킨 거리를 구해서 죄솟값을 구한다.
# 먼저, 치킨집을 찾아서 치킨집 리스트에 넣고, 집을 찾아서 집 리스트에 넣는다.
# m개의 조합을 사용하여 치킨집 조합과 집 리스트를 이중 for문으로 돌려 거리를 구한다.

### 시간 복잡도
# 모든 2에서 모든 1에 대한 거리를 계산해야 하니까 O(2의 개수 * 1의 개수)

### 자료구조
# 1. 집 리스트
# 2. 치킨집 리스트

import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(n))
result = 999999
house = []
chick = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chick.append([i, j])

for chi in combinations(chick, m):
    temp = 0
    for h in house:
        chi_len = 999
        for j in range(m):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chi_len
    result = min(result, temp)

print(result)



