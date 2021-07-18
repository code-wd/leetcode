"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。
注意：解集不能包含重复的组合。

链接：https://leetcode-cn.com/problems/combination-sum-ii
"""


class Solution:
    def combinationSum2(self, candidates, target):
        res = []

        if sum(candidates) < target:
            return []

        def backtrack(nums, bag_nums, goal_num, start_index):
            # 递归边界条件
            if sum(bag_nums) == goal_num:
                res.append(bag_nums)
            if sum(bag_nums) > goal_num:
                return

            for i in range(start_index, len(nums)):
                # 这个去重操作比较抽象，实际上就是在原来已经有的基础上
                # 这一层添加的数字的操作，如果这个数字不是第一次出现，那就直接跳过
                if i > start_index and nums[i] == nums[i - 1]:
                    continue
                backtrack(nums, bag_nums + [nums[i]], goal_num, i + 1)

        num_list = sorted(candidates)
        backtrack(num_list, [], target, 0)
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(solution.combinationSum2(nums, target))
