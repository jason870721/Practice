# const
MAX_INT = (2<<30) -1
MIN_INT = - 2<<30

def reverse(x: int) -> int:
    isNegative = x<0
    x = abs(x)
    result = 0

    while True:
        reminder = x % 10
        x = x // 10
        result = result * 10 + reminder
        if x == 0:
            break

    if isNegative:
        result = result * -1

    print("result: ", result)

    if result > MAX_INT or result < MIN_INT:
        return 0

    return result



def test_max_min_int():
    print(MAX_INT)
    print(MIN_INT)

def test_positive_number():
    assert reverse(123) == 321


def test_negative_number():
    assert reverse(-123) == -321


def test_with_trailing_zero():
    assert reverse(120) == 21


def test_overflow_positive():
    assert reverse(1534236469) == 0


def test_overflow_negative():
    assert reverse(-1563847412) == 0


def test_single_digit():
    assert reverse(5) == 5


def test_zero():
    assert reverse(0) == 0