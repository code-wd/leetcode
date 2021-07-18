"""
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。

链接：https://leetcode-cn.com/problems/first-missing-positive/
"""


class Solution:
    def firstMissingPositive(self, nums):
        if len(nums) < 1:
            return 1
        i = 0
        while i < len(nums):
            if nums[i] <= 0 or nums[i] > len(nums) or nums[i] == i+1:
                i += 1
            else:
                temp = nums[i] - 1
                # 可能出现重复的数字，防止陷入死循环
                if nums[temp] == nums[i]:
                    i += 1
                    continue

                nums[i], nums[temp] = nums[temp], nums[i]

        # 当前值不是 j+1 的就是要找的数字
        for j in range(len(nums)):
            if nums[j] != j + 1:
                return j+1
        return len(nums)+1


if __name__ == '__main__':
    solution = Solution()
    nums = [7,8,9,11,12]
    print(solution.firstMissingPositive(nums))