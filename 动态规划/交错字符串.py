"""
给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。
两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
提示：a + b 意味着字符串 a 和 b 连接

链接：https://leetcode-cn.com/problems/interleaving-string
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, l = len(s1), len(s2), len(s3)

        # if m + n != l:
        #     return False

        dp = [[[False] * (m+1) for i in range(n+1)] for _ in range(l+1)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][j][i] = True
                else:
                    dp[0][j][i] = False

        for i in range(1, l):
            for j in range(n):
                k = i - j
                if j >= 1 and dp[i-1][j-1][k] and s3[i] == s2[j]:
                    dp[i][j][k] = True
                if k >= 1 and dp[i-1][j][k-1] and s3[i] == s1[k]:
                    dp[i][j][k] = True

        return dp[l-1][n-1][m-1]


if __name__ == '__main__':
    solution = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(solution.isInterleave(s1, s2, s3))
