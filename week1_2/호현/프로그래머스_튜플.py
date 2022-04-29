import re
from collections import Counter

def solution(s):
    L = re.findall('[\d]+', s)
    L = Counter(L).most_common()
    return [int(i[0]) for i in L]