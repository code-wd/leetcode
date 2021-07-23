"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

链接：https://leetcode-cn.com/problems/maximum-subarray/
"""


class Solution:
    def maxSubArray(self, nums) -> int:
        """
        动态规划
        :param nums:
        :return:
        """
        dp = nums[0]
        res = dp

        for i in range(1, len(nums)):
            dp = max(nums[i], dp + nums[i])
            res = max(dp, res)
        return res


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    solution = Solution()
    print(solution.maxSubArray(nums))
