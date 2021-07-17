"""
题目：15
给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

链接： https://leetcode-cn.com/problems/3sum/
"""


class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []

        # 首先，对数组进行排序
        nums_sorted = sorted(nums)
        res = []

        for first in range(len(nums_sorted)):
            # 确保第一个指针对应的数字与上一轮是不重复的；这样做是为了避免重复三元组
            if first == 0 or nums_sorted[first] > nums_sorted[first-1]:
                # 因为第二和第三指针符合：第二个指针对应数字增加必然导致第三个指针对应数字减小
                # 因此这里可以使用双指针方法
                second, third = first + 1, len(nums_sorted) - 1

                while second < third:
                    while nums_sorted[first] + nums_sorted[second] + nums_sorted[third] > 0:
                        third -= 1

                        if third == second:
                            break
                    if third == second:
                        break

                    if nums_sorted[first] + nums_sorted[second] + nums_sorted[third] == 0:
                        res.append([nums_sorted[first], nums_sorted[second], nums_sorted[third]])

                    while second < third and nums_sorted[second] == nums_sorted[second+1]:
                        second += 1
                    second += 1

        return res


if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    solution = Solution()
    print(solution.threeSum(nums))
