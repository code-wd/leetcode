"""
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数。
你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符

链接：https://leetcode-cn.com/problems/edit-distance
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            dp[i][0] = i
        for i in range(1, n+1):
            dp[0][i] = i

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1])
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        return dp[m][n]


if __name__ == '__main__':
    solution = Solution()
    word1 = "horse"
    word2 = "ros"
    print(solution.minDistance(word1, word2))
