"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

链接：https://leetcode-cn.com/problems/trapping-rain-water/
"""


class Solution:
    def trap(self, height) -> int:
        left, right = [], []
        left_max, right_max = 0, 0

        for i in range(len(height)):
            left.append(left_max)
            left_max = max(left_max, height[i])

        for i in range(len(height)):
            right.append(right_max)
            right_max = max(right_max, height[len(height)-1-i])

        right = right[::-1]
        res = 0

        for i in range(len(height)):
            if height[i] < min(left[i], right[i]):
                res += min(left[i], right[i]) - height[i]
        return res


if __name__ == '__main__':
    heights = [0,1,0,2,1,0,1,3,2,1,2,1]
    so = Solution()
    print(so.trap(heights))