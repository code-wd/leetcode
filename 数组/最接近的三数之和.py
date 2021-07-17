"""
题目： 16
给定一个包括n 个整数的数组nums和 一个目标值target。
找出nums中的三个整数，使得它们的和与target最接近。返回这三个数的和。
假定每组输入只存在唯一答案

链接：https://leetcode-cn.com/problems/3sum-closest
"""
import sys


class Solution:
    def threeSumClosest(self, nums, target):
        nums_sorted = sorted(nums)
        res = sys.maxsize
        result = None

        # 外层循环，指针 first
        for first in range(len(nums) - 2):
            if first == 0 or nums_sorted[first] != nums_sorted[first - 1]:
                # 第二层循环，使用双指针
                second, third = first + 1, len(nums) - 1
                while second < third:
                    sum_of_nums = nums_sorted[first] + nums_sorted[second] + nums_sorted[third]
                    if abs(sum_of_nums - target) < res:
                        res = abs(sum_of_nums - target)
                        result = sum_of_nums
                    # 指针更替条件
                    if sum_of_nums > target:
                        third -= 1
                    elif sum_of_nums < target:
                        second += 1
                    else:
                        return result
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 2, 1, -4]
    target = 1
    print(solution.threeSumClosest(nums, target))
