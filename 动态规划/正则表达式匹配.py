"""
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

链接：https://leetcode-cn.com/problems/regular-expression-matching/
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        使用动态规划的方法，dp 数组的含义比较简单，容易想出来
        但是问题是状态转移方程比较复杂，需要考虑很多不同的情况
        :param s:
        :param p:
        :return:
        """
        m, n = len(s), len(p)

        # 设置 dp 数组，数组的大小为 (m+1, n+1)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # 表示当两个字符串都是空的时候，是匹配的

        def matches(i, j):
            if i == 0:  # 考虑边界情况，因为 dp[i][j] 实际上是考虑的 i-1，j-1 位置的字符
                return False
            if p[j-1] == ".":
                return True
            return s[i-1] == p[j-1]

        for i in range(m+1):
            # 这里考虑从 1 开始，因为当 p 为空，而 s 不是空的时候，必然是 False
            for j in range(1, n+1):
                if p[j-1] == "*":
                    dp[i][j] |= dp[i][j-2]

                    if matches(i, j-1):
                        dp[i][j] |= dp[i-1][j]
                else:
                    if matches(i, j):
                        dp[i][j] = dp[i-1][j-1]
        return dp[m][n]


if __name__ == '__main__':
    s = "ab"
    p = ".*"
    solution = Solution()
    print(solution.isMatch(s, p))
