"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

链接：https://leetcode-cn.com/problems/generate-parentheses/
"""


# class Solution:
#     def generateParenthesis(self, n: int):
#         """
#         动态规划
#         :param n:
#         :return:
#         """
#         if n == 0:
#             return []
#         if n == 1:
#             return ["()"]
#
#         dp = [[None], ["()"]]
#
#         for i in range(2, n+1):
#             cur_list = []
#
#             for j in range(i):
#                 left_list = dp[j]
#                 right_list = dp[i-1-j]
#
#                 for left in left_list:
#                     for right in right_list:
#                         if left is None:
#                             cur_list.append("()" + right)
#                         elif right is None:
#                             cur_list.append("(" + left + ")")
#                         else:
#                             cur_list.append("(" + left + ")" + right)
#             dp.append(cur_list)
#         return dp[-1]

class Solution:
    def generateParenthesis(self, n: int):
        """
        回溯算法
        :param n:
        :return:
        """
        if n == 0:
            return []

        res = []

        def back_trace(cur_s, left_num, right_num):
            if right_num < left_num:
                return
            if left_num == right_num == 0:
                res.append(cur_s)

            if left_num > 0:
                back_trace(cur_s + "(", left_num - 1, right_num)
            if right_num > 0:
                back_trace(cur_s + ")", left_num, right_num - 1)

        back_trace("", n, n)
        return res


if __name__ == '__main__':
    solution = Solution()
    n = 2
    print(solution.generateParenthesis(n))