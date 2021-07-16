# coding=utf-8
"""
题目：11

给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水

链接：https://leetcode-cn.com/problems/container-with-most-water/
"""


class Solution(object):
    def maxArea(self, height):
        """
        直接使用暴力的算法，时间复杂度为 n * n
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0

        max_area = 0

        for i in range(len(height)):
            for j in range(i, len(height)):
                cur_area = (j - i) * min(height[i], height[j])
                max_area = max(cur_area, max_area)
        return max_area

    def max_area(self, height):
        """
        使用双指针的思想，时间复杂度为 n
        :param height:
        :return:
        """
        if len(height) < 2:
            return 0

        left = 0
        right = len(height) - 1
        max_a = (right - left) * min(height[left], height[right])

        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            max_a = max(max_a, (right - left) * min(height[left], height[right]))
        return max_a


if __name__ == '__main__':
    heights = [4, 3, 2, 1, 4]
    solution = Solution()
    print(solution.maxArea(heights))
