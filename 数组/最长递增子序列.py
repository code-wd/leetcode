"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
"""


# class Solution:
#     def lengthOfLIS(self, nums) -> int:
#         if len(nums) == 0:
#             return 0
#         if len(nums) == 1:
#             return 1
#
#         dp = [1 for i in range(len(nums))]
#
#         for i in range(1, len(nums)):
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#
#         return max(dp)


class Solution:
    def lengthOfLIS(self, nums) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        def binary_search(num_list, left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if num_list[mid] == target:
                    return mid
                elif num_list[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        dp = []

        for i in range(len(nums)):
            if len(dp) == 0 or nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                index = binary_search(dp, 0, len(dp)-1, nums[i])
                dp[index] = nums[i]
        return len(dp)


if __name__ == '__main__':
    solution = Solution()
    nums = [3,5,6,2,5,4,19,5,6,7,12]
    print(solution.lengthOfLIS(nums))