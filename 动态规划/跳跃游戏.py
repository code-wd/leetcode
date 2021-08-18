"""
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标。

链接：https://leetcode-cn.com/problems/jump-game/
"""

class Solution:
    def canJump(self, nums) -> bool:
        length = len(nums)

        # 两个边界情况
        if length == 1 or 0 not in nums:
            return True
        if nums[0] == 0:
            return False

        left = [-1 for _ in range(length)]
        zero_point = -1
        zero_dict = {}

        for i in range(length):
            cur_index = length - 1 - i

            if nums[cur_index] == 0:
                zero_point = cur_index
                zero_dict[zero_point] = False
            else:
                left[cur_index] = zero_point

        for i in range(length):
            if left[i] == -1:
                continue

            if nums[i] + i > left[i]:
                zero_dict[left[i]] = True

        for key in zero_dict:
            if not zero_dict[key]:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    nums = [2,3,1,1,4]
    print(solution.canJump(nums))

