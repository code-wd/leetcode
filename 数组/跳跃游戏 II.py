"""
给你一个非负整数数组 nums ，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
假设你总是可以到达数组的最后一个位置。

链接：https://leetcode-cn.com/problems/jump-game-ii
"""


class Solution:
    def jump(self, nums) -> int:
        """
        使用贪心算法
        :param nums: 给定的数组
        :return: 返回最少需要的步数
        """

        max_pos, step, end = 0, 0, 0

        for i in range(len(nums) - 1):
            if max_pos >= i:
                max_pos = max(max_pos, nums[i] + i)

                if i == end:
                    end = max_pos
                    step += 1
        return step


if __name__ == '__main__':
    solution = Solution()
    nums = [2,3,1,1,4]
    print(solution.jump(nums))