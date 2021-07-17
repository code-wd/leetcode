"""
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
"""


class Solution:
    def removeDuplicates(self, nums):
        slow, fast = 0, 0

        while fast < len(nums):
            while fast < len(nums) and nums[fast] == nums[slow]:
                fast += 1

            if fast < len(nums):
                nums[slow + 1] = nums[fast]
                slow += 1
        # 删除多余的元素
        while len(nums) > slow + 1:
            nums.pop()

        return len(nums)


if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,2]
    solution.removeDuplicates(nums)