"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：
你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？

链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
"""


class Solution:
    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]

        left1, left2, right1, right2 = 0, 0, len(nums) - 1, len(nums) - 1

        while left1 <= right1:
            mid = (left1 + right1) // 2

            if nums[mid] >= target:
                right1 = mid - 1
            else:
                left1 = mid + 1

        while left2 <= right2:
            mid = (left2 + right2) // 2

            if nums[mid] <= target:
                left2 = mid + 1
            else:
                right2 = mid - 1
        if left1 < len(nums) and nums[left1] == target:
            return [left1, right2]
        else:
            return [-1, -1]


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 2]
    target = 3
    print(solution.searchRange(nums, target))