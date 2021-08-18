"""
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
注意:
假设字符串的长度不会超过 1010。

示例 1:
输入:
"abccccdd"
输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。

链接：https://leetcode-cn.com/problems/longest-palindrome
"""

class Solution:
    def longestPalindrome(self, s):
        s_dict = {}

        for item in s:
            if item in s_dict:
                s_dict[item] += 1
            else:
                s_dict[item] = 1
        res = 0
        flag = False

        for key in s_dict:
            res += s_dict[key] // 2 * 2
            if not flag and s_dict[key] % 2 == 1:
                flag = True

        if flag:
            res += 1
        return res