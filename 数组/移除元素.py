"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

链接：https://leetcode-cn.com/problems/remove-element
"""


# 方法一：直接删除
# class Solution:
#     def removeElement(self, nums, val):
#         while val in nums:
#             nums.remove(val)
#         return len(nums)

# 方法二：双指针
class Solution:
    def removeElement(self, nums, val):
        left, right = 0, len(nums) - 1

        while right > left:
            while right > left and nums[right] != val:
                right -= 1
            if right <= left:
                break
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

        while len(nums) > 0 and nums[0] == val:
            nums.pop(0)
        return len(nums)


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 3]
    val = 5
    solution.removeElement(nums, val)