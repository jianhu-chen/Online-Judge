# 第 329 场周赛

> 企业: 力扣

## 2544.交替数字和

[打开力扣](https://leetcode.cn/problems/alternating-digit-sum) [我的代码](2544.alternating_digit_sum.py)

给你一个正整数 <code>n</code> 。<code>n</code> 中的每一位数字都会按下述规则分配一个符号：

<ul>
	<li><strong>最高有效位</strong> 上的数字分配到 <strong>正</strong> 号。</li>
	<li>剩余每位上数字的符号都与其相邻数字相反。</li>
</ul>

返回所有数字及其对应符号的和。



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>n = 521
<strong>输出：</strong>4
<strong>解释：</strong>(+5) + (-2) + (+1) = 4</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>n = 111
<strong>输出：</strong>1
<strong>解释：</strong>(+1) + (-1) + (+1) = 1
</pre>

<strong>示例 3：</strong>

<pre>
<strong>输入：</strong>n = 886996
<strong>输出：</strong>0
<strong>解释：</strong>(+8) + (-8) + (+6) + (-9) + (+9) + (-6) = 0
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= n <= 10<sup>9</sup></code></li>
</ul>

## 2545.根据第 K 场考试的分数排序

[打开力扣](https://leetcode.cn/problems/sort-the-students-by-their-kth-score) [我的代码](2545.sort_the_students_by_their_kth_score.py)

班里有 <code>m</code> 位学生，共计划组织 <code>n</code> 场考试。给你一个下标从 <strong>0</strong> 开始、大小为 <code>m x n</code> 的整数矩阵 <code>score</code> ，其中每一行对应一位学生，而 <code>score[i][j]</code> 表示第 <code>i</code> 位学生在第 <code>j</code> 场考试取得的分数。矩阵 <code>score</code> 包含的整数<strong>互不相同</strong>。

另给你一个整数 <code>k</code> 。请你按第 <code>k</code> 场考试分数从高到低完成对这些学生（矩阵中的行）的排序。

返回排序后的矩阵。



<strong>示例 1：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/11/30/example1.png" style="width: 600px; height: 136px;" />

<pre>
<strong>输入：</strong>score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]], k = 2
<strong>输出：</strong>[[7,5,11,2],[10,6,9,1],[4,8,3,15]]
<strong>解释：</strong>在上图中，S 表示学生，E 表示考试。
- 下标为 1 的学生在第 2 场考试取得的分数为 11 ，这是考试的最高分，所以 TA 需要排在第一。
- 下标为 0 的学生在第 2 场考试取得的分数为 9 ，这是考试的第二高分，所以 TA 需要排在第二。
- 下标为 2 的学生在第 2 场考试取得的分数为 3 ，这是考试的最低分，所以 TA 需要排在第三。
</pre>

<strong>示例 2：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/11/30/example2.png" style="width: 486px; height: 121px;" />

<pre>
<strong>输入：</strong>score = [[3,4],[5,6]], k = 0
<strong>输出：</strong>[[5,6],[3,4]]
<strong>解释：</strong>在上图中，S 表示学生，E 表示考试。
- 下标为 1 的学生在第 0 场考试取得的分数为 5 ，这是考试的最高分，所以 TA 需要排在第一。
- 下标为 0 的学生在第 0 场考试取得的分数为 3 ，这是考试的最低分，所以 TA 需要排在第二。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>m == score.length</code></li>
	<li><code>n == score[i].length</code></li>
	<li><code>1 <= m, n <= 250</code></li>
	<li><code>1 <= score[i][j] <= 10<sup>5</sup></code></li>
	<li><code>score</code> 由 <strong>不同</strong> 的整数组成</li>
	<li><code>0 <= k < n</code></li>
</ul>

## 2546.执行逐位运算使字符串相等

[打开力扣](https://leetcode.cn/problems/apply-bitwise-operations-to-make-strings-equal) [我的代码](2546.apply_bitwise_operations_to_make_strings_equal.py)

给你两个下标从 <strong>0</strong> 开始的 <strong>二元</strong> 字符串 <code>s</code> 和 <code>target</code> ，两个字符串的长度均为 <code>n</code> 。你可以对 <code>s</code> 执行下述操作 <strong>任意</strong> 次：

<ul>
	<li>选择两个 <strong>不同</strong> 的下标 <code>i</code> 和 <code>j</code> ，其中 <code>0 <= i, j < n</code> 。</li>
	<li>同时，将 <code>s[i]</code> 替换为 (<code>s[i]</code> <strong>OR</strong> <code>s[j]</code>) ，<code>s[j]</code> 替换为 (<code>s[i]</code> <strong>XOR</strong> <code>s[j]</code>) 。</li>
</ul>

例如，如果 <code>s = "0110"</code> ，你可以选择 <code>i = 0</code> 和 <code>j = 2</code>，然后同时将 <code>s[0]</code> 替换为 (<code>s[0]</code> <strong>OR</strong> <code>s[2]</code> = <code>0</code> <strong>OR</strong> <code>1</code> = <code>1</code>)，并将 <code>s[2]</code> 替换为 (<code>s[0]</code> <strong>XOR</strong> <code>s[2]</code> = <code>0</code> <strong>XOR</strong> <code>1</code> = <code>1</code>)，最终得到 <code>s = "1110"</code> 。

如果可以使 <code>s</code> 等于 <code>target</code> ，返回 <code>true</code> ，否则，返回 <code>false</code> 。



<strong>示例 1：</strong>

<pre><strong>输入：</strong>s = "1010", target = "0110"
<strong>输出：</strong>true
<strong>解释：</strong>可以执行下述操作：
- 选择 i = 2 和 j = 0 ，得到 s = "<em><strong>0</strong></em>0<em><strong>1</strong></em>0".
- 选择 i = 2 和 j = 1 ，得到 s = "0<em><strong>11</strong></em>0".
可以使 s 等于 target ，返回 true 。
</pre>

<strong>示例 2：</strong>

<pre><strong>输入：</strong>s = "11", target = "00"
<strong>输出：</strong>false
<strong>解释：</strong>执行任意次操作都无法使 s 等于 target 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>n == s.length == target.length</code></li>
	<li><code>2 <= n <= 10<sup>5</sup></code></li>
	<li><code>s</code> 和 <code>target</code> 仅由数字 <code>0</code> 和 <code>1</code> 组成</li>
</ul>

## 2547.拆分数组的最小代价

[打开力扣](https://leetcode.cn/problems/minimum-cost-to-split-an-array) [我的代码](2547.minimum_cost_to_split_an_array.py)

给你一个整数数组 <code>nums</code> 和一个整数 <code>k</code> 。

将数组拆分成一些非空子数组。拆分的 <strong>代价</strong> 是每个子数组中的 <strong>重要性</strong> 之和。

令 <code>trimmed(subarray)</code> 作为子数组的一个特征，其中所有仅出现一次的数字将会被移除。

<ul>
	<li>例如，<code>trimmed([3,1,2,4,3,4]) = [3,4,3,4]</code> 。</li>
</ul>

子数组的 <strong>重要性</strong> 定义为 <code>k + trimmed(subarray).length</code> 。

<ul>
	<li>例如，如果一个子数组是 <code>[1,2,3,3,3,4,4]</code> ，<code>trimmed([1,2,3,3,3,4,4]) = [3,3,3,4,4]</code> 。这个子数组的重要性就是 <code>k + 5</code> 。</li>
</ul>

找出并返回拆分 <code>nums</code> 的所有可行方案中的最小代价。

<strong>子数组</strong> 是数组的一个连续 <strong>非空</strong> 元素序列。



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>nums = [1,2,1,2,1,3,3], k = 2
<strong>输出：</strong>8
<strong>解释：</strong>将 nums 拆分成两个子数组：[1,2], [1,2,1,3,3]
[1,2] 的重要性是 2 + (0) = 2 。
[1,2,1,3,3] 的重要性是 2 + (2 + 2) = 6 。
拆分的代价是 2 + 6 = 8 ，可以证明这是所有可行的拆分方案中的最小代价。
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>nums = [1,2,1,2,1], k = 2
<strong>输出：</strong>6
<strong>解释：</strong>将 nums 拆分成两个子数组：[1,2], [1,2,1] 。
[1,2] 的重要性是 2 + (0) = 2 。
[1,2,1] 的重要性是 2 + (2) = 4 。
拆分的代价是 2 + 4 = 6 ，可以证明这是所有可行的拆分方案中的最小代价。
</pre>

<strong>示例 3：</strong>

<pre>
<strong>输入：</strong>nums = [1,2,1,2,1], k = 5
<strong>输出：</strong>10
<strong>解释：</strong>将 nums 拆分成一个子数组：[1,2,1,2,1].
[1,2,1,2,1] 的重要性是 5 + (3 + 2) = 10 。
拆分的代价是 10 ，可以证明这是所有可行的拆分方案中的最小代价。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length <= 1000</code></li>
	<li><code>0 <= nums[i] < nums.length</code></li>
	<li><code>1 <= k <= 10<sup>9</sup></code></li>
</ul>
