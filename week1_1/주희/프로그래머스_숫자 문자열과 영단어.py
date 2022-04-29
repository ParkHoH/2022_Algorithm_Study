### 문제
# 일부 자릿수를 영단어로 카드 (예. 1478 -> "one4seveneight")
# s가 의미하는 원래 숫자를 return 하도록

### 입력
# s : 1<= s <= 50 (이 때, s가 0 또는 zero로 시작하지 않음)

### 출력
# result : 1 <= result <= 2,000,000,000 의 정수

### 아이디어
# 1. 먼저, 영단어랑 숫자를 조합한 딕셔너리를 만들어준다.
# 2. s가 숫자면, result에 그대로 넣어주고, 문자면 word에 넣어줘서 딕셔너리 안에 있는 영단어와 매치되면, result에 넣어준다.
# 3. result에 넣어준 후, word는 초기화 시켜준다.

### 시간 복잡도
# 1. s를 하나씩 모두 탐색하는 것이니까, O(s)

### 자료구조
# 1. answer = ""(결과값)
# 2. number = {} (영단어, 숫자 매칭되는 딕셔너리)
# 3. word = "" (s에서 문자열만 뺴서 담기)

def solution(s):
    answer = ""
    number = { "zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9 }
    word = ""
    for i in s:
        if i.isdigit():
            answer += str(i)
        else:
            word += i
            if word in number:
                answer += str(number[word])
                word = ""
    return int(answer)