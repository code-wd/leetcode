"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。

链接：https://leetcode-cn.com/problems/combination-sum
"""
import copy


class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def track(nums, bag_nums, goal_num):
            # 递归边界条件
            if sum(bag_nums) == goal_num:
                res.append(bag_nums)
            if sum(bag_nums) > goal_num:
                return

            # 做出选择、递归、撤销选择
            for i in range(len(nums)):
                track(nums[i:], bag_nums + [nums[i]], goal_num)

        track(candidates, [], target)
        return res


if __name__ == '__main__':
    solution = Solution()
    candidates = [2,3,5]
    target = 8
    print(solution.combinationSum(candidates, target))

