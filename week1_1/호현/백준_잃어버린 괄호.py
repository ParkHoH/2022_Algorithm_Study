s = input().split("-")
result = 0
for i in range(len(s)):
    for j in s[i].split("+"):
        result += -int(j) if i else int(j)
print(result)