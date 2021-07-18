"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str):
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        char_dict = {}
        dp = [1 for i in range(len(s))]

        for i in range(len(s)):
            if s[i] not in char_dict:
                char_dict[s[i]] = i

                if i == 0:
                    continue
                else:
                    dp[i] = dp[i-1] + 1
            else:
                # 如果这个 char 在原来出现过，则当前位置结尾的最长无重复子串的最长长度
                # 应该取 dp[i-1]+1 和 当前位置与上一个出现位置之间距离的较小值
                dp[i] = min(dp[i-1] + 1, i - char_dict[s[i]])
                char_dict[s[i]] = i

        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    s = "pwwkew"
    print(solution.lengthOfLongestSubstring(s))