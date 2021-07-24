"""
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

链接：https://leetcode-cn.com/problems/maximum-product-subarray/
"""
import sys


class Solution:
    def maxProduct(self, nums) -> int:
        l = len(nums)
        dp_max = nums[0]
        dp_min = nums[0]

        res = max(nums)

        for i in range(1, l):
            temp_max = max(dp_max * nums[i], dp_min * nums[i], nums[i])
            temp_min = min(dp_max * nums[i], dp_min * nums[i], nums[i])
            dp_max, dp_min = temp_max, temp_min
            res = max(res, dp_max)
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [-2,-3,-4]
    print(solution.maxProduct(nums))