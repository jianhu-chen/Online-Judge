## 回溯

回溯算法是对树形或者图形结构执行一次深度优先遍历，实际上类似枚举的搜索尝试过程，在遍历的过程中寻找问题的解。

深度优先遍历有个特点：当发现已不满足求解条件时，就返回，尝试别的路径。此时对象类型变量就需要重置成为和之前一样，称为「状态重置」。

许多复杂的，规模较大的问题都可以使用回溯法，有「通用解题方法」的美称。实际上，回溯算法就是暴力搜索算法，它是早期的人工智能里使用的算法，借助计算机强大的计算能力帮助我们找到问题的解。

[力扣相关题目](https://leetcode.cn/tag/backtracking/problemset/)


## 典型题目

- [x] [汉诺塔问题](hanota.py)
  
- [x] [全排列](permutations.py)

- [x] [全排列 (含重复值)](permutations_v2.py)

- [x] [N-Queens问题](../greedy/n_queens.py)

- [x] [机器人走步](../dp/robot_walk.py)

- [x] [纸牌游戏](../dp/cards_in_line.py)

- [x] [背包问题](../dp/knapsack.py)

- [x] [数字字符串转换为字母的方法数](../dp/convert_to_letter_string.py)

- [ ] [贴纸拼词](../dp/stickers_to_spell_word.py)

- [x] [最长公共子序列](../dp/longest_common_subsequence.py)

- [x] [最长回文子序列](../dp/longest_palindromic_subsequence.py)

- [x] [象棋中马的跳法](../dp/horse_jump.py)

- [x] [最小路径和](../dp/min_path_sum.py)

- [x] [零钱兑换1](../dp/min_coins_no_limit.py)

- [x] [零钱兑换2](../dp/coins_way_every_paper_different.py)

- [x] [零钱兑换3](../dp/coins_way_no_limit.py)

- [ ] [零钱兑换4](../dp/coins_way_same_value_same_papper.py)

- [x] [Bob之死](../dp/bob_die.py)

- [x] [打怪兽](../dp/kill_monster.py)

- [ ] [泡咖啡](../dp/coffee.py)

- [x] [数字分裂](../dp/split_number.py)

- [ ] [划分数字1](../dp/split_sum_closed.py)

- [ ] [划分数字2](../dp/split_sum_closed_size_half.py)
