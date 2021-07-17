"""
给定一个包含 n 个整数的数组nums和一个目标值 target，
判断 nums 中是否存在四个元素 a，b，c和 d，
使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：答案中不可以包含重复的四元组。

链接：https://leetcode-cn.com/problems/4sum
"""


class Solution:
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []

        nums_sorted = sorted(nums)
        result = []

        # 第一个指针的位置
        for first in range(len(nums) - 3):
            # 下面两个 if 语句是用于剪枝操作
            if nums_sorted[first] + nums_sorted[first + 1] + nums_sorted[first + 2] + nums_sorted[first + 3] > target:
                break
            if nums_sorted[first] + nums_sorted[len(nums) - 1] + \
                    nums_sorted[len(nums) - 2] + nums_sorted[len(nums) - 3] < target:
                continue

            if first != 0 and nums_sorted[first] == nums_sorted[first - 1]:
                continue
            # 第二个指针的位置
            for second in range(first + 1, len(nums) - 2):
                if second != first + 1 and nums_sorted[second] == nums_sorted[second - 1]:
                    continue

                # 第三和第四个指针，是双指针
                # 其中的 while 循环是为了去除重复
                third, forth = second + 1, len(nums) - 1

                while third < forth:
                    if nums_sorted[first] + nums_sorted[second] + nums_sorted[third] + nums_sorted[forth] > target:
                        while forth > third and nums_sorted[forth - 1] == nums_sorted[forth]:
                            forth -= 1
                        forth -= 1
                    elif nums_sorted[first] + nums_sorted[second] + nums_sorted[third] + nums_sorted[forth] < target:
                        while third < forth and nums_sorted[third + 1] == nums_sorted[third]:
                            third += 1
                        third += 1
                    else:
                        result.append([nums_sorted[first], nums_sorted[second],
                                       nums_sorted[third], nums_sorted[forth]])

                        while forth > third and nums_sorted[forth - 1] == nums_sorted[forth]:
                            forth -= 1
                        while third < forth and nums_sorted[third + 1] == nums_sorted[third]:
                            third += 1
                        forth -= 1
                        third += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(solution.fourSum(nums, target))
