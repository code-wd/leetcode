"""
请你判断一个 9x9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
数独部分空格内已填入了数字，空白格用 '.' 表示。

注意：
一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。

链接：https://leetcode-cn.com/problems/valid-sudoku
"""


class Solution:
    def isValidSudoku(self, board) -> bool:
        row_dict = [{} for i in range(9)]
        col_dict = [{} for i in range(9)]
        box_dict = [{} for i in range(9)]

        res = True

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row_dict[i]:
                    return False
                if board[i][j] in col_dict[j]:
                    return False

                row_dict[i][board[i][j]] = 1
                col_dict[j][board[i][j]] = 1

                box = j // 3 * 3 + i // 3
                if board[i][j] in box_dict[box]:
                    return False
                box_dict[box][board[i][j]] = 1

        return True


if __name__ == '__main__':
    board = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],
             [".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],
             [".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],
             [".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],
             [".",".","4",".",".",".",".",".","."]]
    solution = Solution()
    print(solution.isValidSudoku(board))