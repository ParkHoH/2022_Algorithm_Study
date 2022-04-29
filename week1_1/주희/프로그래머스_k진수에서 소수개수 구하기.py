### 아이디어
# 1. 먼저, k진수로 바꾼다.
# 2. 0을 기준으로 분리시킨다.
# 3. 소수가 맞는지 확인한다.

import math

def convert_num(n, k):
    result = ''
    while n > 0:
        n, mod = divmod(n, k)
        result += str(mod)
    return result[::-1]

def prime_num(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    n = convert_num(n,k)
    split_list = n.split('0')
    for i in split_list:
        if i:
            if int(i) == 1:
                continue
            elif prime_num(int(i)):
                answer += 1
    return answer
