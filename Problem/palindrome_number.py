class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        while rev < x:
            rev = rev * 10 + x % 10
            x //= 10

        # 比較反轉的一半與剩下的一半
        return x == rev or x == rev // 10


def test_1():
    assert Solution.isPalindrome(121) == True

def test_2():
    assert Solution.isPalindrome(-123) == False

def test_3():
    assert Solution.isPalindrome(10) == False

def test_4():
    assert Solution.isPalindrome(0) == True