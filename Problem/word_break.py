from typing import List


class Solution:
    @staticmethod
    def wordBreak(s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]


def test_1():
    assert Solution.wordBreak("leetcode", ["leet","code"]) == True

def test_2():
    assert Solution.wordBreak("applepenapple", ["apple","pen"]) == True

def test_3():
    assert Solution.wordBreak("catsandog", ["cats","dog","sand","and","cat"]) == False