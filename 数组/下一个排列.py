"""
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须 原地 修改，只允许使用额外常数空间。

链接：https://leetcode-cn.com/problems/next-permutation

"""
import sys


class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        if len(nums) == 2:
            nums[0], nums[1] = nums[1], nums[0]
            return

        k = len(nums) - 1
        pre = k - 1

        while pre >= 0:
            if nums[pre] >= nums[k]:
                pre -= 1
                k -= 1
            else:
                break

        if pre == -1:
            nums.sort()
            return

        index = len(nums) - 1
        while nums[index] <= nums[pre]:
            index -= 1
        nums[index], nums[pre] = nums[pre], nums[index]
        # 可以证明，nums[pre+1:] 是递减的；当然也可以排序
        nums[pre+1:] = nums[pre+1:][::-1]
        return


if __name__ == '__main__':
    solution = Solution()
    nums = [5,1, 1]
    solution.nextPermutation(nums)
    print(nums)
