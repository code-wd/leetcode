"""
给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：
    输入：s = "babad"
    输出："bab"
    解释："aba" 同样是符合题意的答案。

链接：https://leetcode-cn.com/problems/longest-palindromic-substring/
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        res = s[0]
        max_size = 1
        dp = [[False for i in range(len(s))] for j in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = True

        for col in range(1, len(s)):
            for row in range(col):
                if s[col] != s[row]:
                    continue

                if col - row == 1 or dp[row+1][col-1]:
                    dp[row][col] = True

                    if col - row + 1 > max_size:
                        max_size = col - row + 1
                        res = s[row:col+1]
        return res


if __name__ == '__main__':
    s = "ac"
    solution = Solution()
    print(solution.longestPalindrome(s))