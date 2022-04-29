def solution(n, k):
    s = ''
    while n:
        s += str(n%k)
        n //= k
    s = s[::-1].split("0")
    
    result = 0
    for num in s:
        is_prime = True
        if num:
            for i in range(2, int(int(num)**0.5) + 1):
                if int(num) % i == 0:
                    is_prime = False
                    break
            if int(num) >= 2 and is_prime: 
                result += 1
    
    return result

print(solution(437674,3))