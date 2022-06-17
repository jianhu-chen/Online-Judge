# -*- coding: utf-8 -*-


class RobotWalk:
    """
    假设有排成一行的N个位置记为1~N, N一定大于或等于2
    开始时机器人在其中的M位置上(M一定是1~N中的一个)
    如果机器人来到1位置, 那么下一步只能往右来到2位置;
    如果机器人来到N位置, 那么下一步只能往左来到N-1位置;
    如果机器人来到中间位置, 那么下一步可以往左走或者往右走;
    规定机器人必须走K步, 最终能来到P位置(P也是1~N中的一个)的方法有多少种
    给定四个参数 N、M、K、P, 返回方法数
    """

    def solution_recursion(self, N, rest, start, end):
        if N < 2 or start < 1 or start > N or end < 1 or end > N:
            return -1

        return self.recursion_process(N, rest, start, end)

    def recursion_process(self, N, rest, start, end):
        if rest == 0:
            return 1 if start == end else 0

        if start == 1:
            return self.recursion_process(N, rest - 1, start + 1, end)
        elif start == N:
            return self.recursion_process(N, rest - 1, start - 1, end)
        else:
            return self.recursion_process(N, rest - 1, start + 1, end) + \
                self.recursion_process(N, rest - 1, start - 1, end)

    def solution_memory_search(self, N, rest, start, end):
        if N < 2 or start < 1 or start > N or end < 1 or end > N:
            return -1

        # row (rest) range: [0, rest], col(start) range: [1, N]
        dp = [[-1 for _ in range(N + 1)] for _ in range(rest + 1)]
        return self.memory_search_process(N, rest, start, end, dp)

    def memory_search_process(self, N, rest, start, end, dp):
        if dp[rest][start] != -1:
            return dp[rest][start]

        if rest == 0:
            ans = 1 if start == end else 0
        elif start == 1:
            ans = self.memory_search_process(N, rest - 1, start + 1, end, dp)
        elif start == N:
            ans = self.memory_search_process(N, rest - 1, start - 1, end, dp)
        else:
            ans = self.memory_search_process(N, rest - 1, start + 1, end, dp) + \
                self.memory_search_process(N, rest - 1, start - 1, end, dp)
        dp[rest][start] = ans

        return ans

    def solution_dp(self, N, rest, start, end):
        if N < 2 or start < 1 or start > N or end < 1 or end > N:
            return -1

        # row (rest) range: [0, rest], col(start) range: [1, N]
        dp = [[0 for _ in range(N + 1)] for _ in range(rest + 1)]
        dp[0][end] = 1
        for i in range(1, rest + 1):
            for j in range(1, N + 1):
                if j != 1:
                    dp[i][j] += dp[i - 1][j - 1]
                if j != N:
                    dp[i][j] += dp[i - 1][j + 1]

        return dp[rest][start]


class CardsInLine:
    """
    给定一个整型数组arr, 代表数值不同的纸牌排成一条线
    玩家A和玩家B依次拿走每张纸牌
    规定玩家A先拿, 玩家B后拿
    但是每个玩家每次只能拿走最左或最右的纸牌
    玩家A和玩家B都绝顶聪明
    请返回最后获胜者的分数
    """

    def solution_recursion(self, arr):
        if not arr:
            return 0

        first_select = self.recursion_first_select(arr, 0, len(arr) - 1)
        second_secect = self.recursion_second_select(arr, 0, len(arr) - 1)
        return max(first_select, second_secect)

    def recursion_first_select(self, arr, start, end):
        if start == end:
            return arr[start]

        return max(
            self.recursion_second_select(arr, start + 1, end) + arr[start],
            self.recursion_second_select(arr, start, end - 1) + arr[end],
        )

    def recursion_second_select(self, arr, start, end):
        if start == end:
            return 0

        return min(
            self.recursion_first_select(arr, start + 1, end),
            self.recursion_first_select(arr, start, end - 1),
        )

    def solution_memory_search(self, arr):
        if not arr:
            return 0

        # row (rest) range: [0, len(arr) - 1], col(start) range: [0, len(arr) - 1]
        dp1 = [[-1 for _ in range(len(arr))] for _ in range(len(arr))]
        dp2 = [[-1 for _ in range(len(arr))] for _ in range(len(arr))]
        first_select = self.memory_search_first_select(arr, 0, len(arr) - 1, dp1, dp2)
        second_secect = self.memory_search_second_select(arr, 0, len(arr) - 1, dp1, dp2)
        return max(first_select, second_secect)

    def memory_search_first_select(self, arr, start, end, dp1, dp2):
        if dp1[start][end] != -1:
            return dp1[start][end]

        if start == end:
            ans = arr[start]
        else:
            ans = max(
                self.memory_search_second_select(arr, start + 1, end, dp1, dp2) + arr[start],
                self.memory_search_second_select(arr, start, end - 1, dp1, dp2) + arr[end]
            )
        dp1[start][end] = ans
        return ans

    def memory_search_second_select(self, arr, start, end, dp1, dp2):
        if dp2[start][end] != -1:
            return dp2[start][end]

        if start == end:
            ans = 0
        else:
            ans = min(
                self.memory_search_first_select(arr, start + 1, end, dp1, dp2),
                self.memory_search_first_select(arr, start, end - 1, dp1, dp2)
            )
        dp2[start][end] = ans
        return ans

    def solution_dp(self, arr):
        if not arr:
            return 0

        # row (rest) range: [0, len(arr) - 1], col(start) range: [0, len(arr) - 1]
        dp1 = [[-1 for _ in range(len(arr))] for _ in range(len(arr))]
        dp2 = [[-1 for _ in range(len(arr))] for _ in range(len(arr))]
        for i in range(len(arr)):
            dp1[i][i] = arr[i]
            dp2[i][i] = 0

        for diff in range(1, len(arr)):
            for i in range(0, len(arr) - diff):
                j = i + diff
                dp1[i][j] = max(dp2[i + 1][j] + arr[i], dp2[i][j - 1] + arr[j])
                dp2[i][j] = min(dp1[i][j - 1], dp1[i + 1][j])

        return max(dp1[0][len(arr) - 1], dp2[0][len(arr) - 1])


class Knapsack:
    """
    给定两个长度都为N的数组weights和values, weights[i]和values[i]分别代表 i号物品的重量和价值
    给定一个正数bag, 表示一个载重bag的袋子, 装的物品不能超过这个重量
    返回能装下的最大价值

    """
    pass


class ConvertToLetterString:
    """
    规定1和A对应、2和B对应、3和C对应...26和Z对应
    那么一个数字字符串比如"111”就可以转化为:
    "AAA"、"KA"和"AK"
    给定一个只有数字字符组成的字符串str,返回有多少种转化结果
    """
    pass


class StickersToSpellWord:
    """
    给定一个字符串str, 给定一个字符串类型的数组arr, 出现的字符都是小写英文
    arr每一个字符串, 代表一张贴纸, 你可以把单个字符剪开使用, 目的是拼出str来
    返回需要至少多少张贴纸可以完成这个任务
    例子: str= "babac", arr = {"ba","c","abcd"}
    ba + ba + c  3  abcd + abcd 2  abcd+ba 2
    所以返回2

    ref: https://leetcode.com/problems/stickers-to-spell-word
    """
    pass


class LongestCommonSubsequence:
    """
    给定两个字符串str1和str2,
    返回这两个字符串的最长公共子序列长度
    比如: str1 = “a12b3c456d”,str2 = “1ef23ghi4j56k”
    最长公共子序列是“123456”, 所以返回长度6

    ref: https://leetcode.com/problems/longest-common-subsequence/
    """
    pass
