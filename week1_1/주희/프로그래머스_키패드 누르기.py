### 문제
# 키패드에서 왼손과 오른손의 엄지 손가락을 이용해서 숫자를 입력하려고 한다.
# 맨 처음, 왼손은 *, 오른손은 # 위치에서 시작한다.
# 1. 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
# 2. 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
# 3. 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
# 4. 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
# 4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.

### 입력
# 순서대로 누를 번호가 담긴 배열 numbers (1 이상 1000이하)
# 왼손잡이인지, 오르손잡이 인지 나타내는 hand

### 출력
# 각 번호를 누른 엄지손가락이 왼손인지, 오른손인지 나타내는 문자열

### 아이디어
# numbers 를 for문 돌리면서, 값이 오른손 쪽인지 왼쪽인지 구분하면서 result에 추가하기
# 만약에 중간쪽 숫자라면, 거리를 계산해야 한다. (거리 계산할때, 딕셔너리로 각 숫자 위치 정보 넣어주기)
# 거리를 계산할 때, 절댓값으로 구하기. 왼쪽 거리와 오른쪽 거리를 각각 구해서, 오른쪽이 더크면 'L'로 추가 한다.
# 만약에 거리가 같다면, hand에 따라 result에 추가해준다.

def position(num, left, right, hand):
    key = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }

    dist_left = abs(key[num][0] - key[left][0]) + abs(key[num][1] - key[left][1])
    dist_right = abs(key[num][0] - key[right][0]) + abs(key[num][1] - key[right][1])

    if dist_left < dist_right:
        return 'L'
    elif dist_left > dist_right:
        return 'R'
    else:
        if hand == 'right':
            return 'R'
        else:
            return 'L'


def solution(numbers, hand):
    answer = ''

    left = '*'
    right = '#'

    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left = num
        elif num in [3, 6, 9]:
            answer += 'R'
            right = num
        else:
            middle = position(num, left, right, hand)
            answer += middle
            if middle == 'R':
                right = num
            else:
                left = num

    return answer