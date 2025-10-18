def myAtoi(s: str) -> int:
    i = 0
    n = len(s)
    while i < n and s[i] == ' ':
        i += 1

    sign = 1
    if i < n and s[i] == '+':
        i += 1
    elif i < n and s[i] == '-':
        sign = -1
        i += 1

    num = 0
    while i < n and s[i].isdigit():
        digit = int(s[i])
        if num > (2**31 - 1 - digit) // 10:
            return 2**31 - 1 if sign == 1 else -2**31
        num = num * 10 + digit
        i += 1

    return sign * num

def test_1():
    assert myAtoi("42") == 42

def test_2():
    assert myAtoi(" -042") == -42

def test_3():
    assert myAtoi("1337c0d3") == 1337

def test_4():
    assert myAtoi("0-1") == 0

def test_5():
    assert myAtoi("words and 987") == 0