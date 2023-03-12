# 第 336 场周赛

> 企业: 力扣 LeetCode

## 6315.统计范围内的元音字符串数

[打开力扣](https://leetcode.cn/problems/count-the-number-of-vowel-strings-in-range) [我的代码](6315.count_the_number_of_vowel_strings_in_range.py)

给你一个下标从 <strong>0</strong> 开始的字符串数组 <code>words</code> 和两个整数：<code>left</code> 和 <code>right</code> 。

如果字符串以元音字母开头并以元音字母结尾，那么该字符串就是一个 <strong>元音字符串</strong> ，其中元音字母是 <code>'a'</code>、<code>'e'</code>、<code>'i'</code>、<code>'o'</code>、<code>'u'</code> 。

返回<em> </em><code>words[i]</code> 是元音字符串的数目，其中<em> </em><code>i</code> 在闭区间 <code>[left, right]</code> 内。



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>words = ["are","amy","u"], left = 0, right = 2
<strong>输出：</strong>2
<strong>解释：</strong>
- "are" 是一个元音字符串，因为它以 'a' 开头并以 'e' 结尾。
- "amy" 不是元音字符串，因为它没有以元音字母结尾。
- "u" 是一个元音字符串，因为它以 'u' 开头并以 'u' 结尾。
在上述范围中的元音字符串数目为 2 。
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4
<strong>输出：</strong>3
<strong>解释：</strong>
- "aeo" 是一个元音字符串，因为它以 'a' 开头并以 'o' 结尾。
- "mu" 不是元音字符串，因为它没有以元音字母开头。
- "ooo" 是一个元音字符串，因为它以 'o' 开头并以 'o' 结尾。
- "artro" 是一个元音字符串，因为它以 'a' 开头并以 'o' 结尾。
在上述范围中的元音字符串数目为 3 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= words.length <= 1000</code></li>
	<li><code>1 <= words[i].length <= 10</code></li>
	<li><code>words[i]</code> 仅由小写英文字母组成</li>
	<li><code>0 <= left <= right < words.length</code></li>
</ul>

## 6316.重排数组以得到最大前缀分数

[打开力扣](https://leetcode.cn/problems/rearrange-array-to-maximize-prefix-score) [我的代码](6316.rearrange_array_to_maximize_prefix_score.py)

给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> 。你可以将 <code>nums</code> 中的元素按 <strong>任意顺序</strong> 重排（包括给定顺序）。

令 <code>prefix</code> 为一个数组，它包含了 <code>nums</code> 重新排列后的前缀和。换句话说，<code>prefix[i]</code> 是 <code>nums</code> 重新排列后下标从 <code>0</code> 到 <code>i</code> 的元素之和。<code>nums</code> 的 <strong>分数</strong> 是 <code>prefix</code> 数组中正整数的个数。

返回可以得到的最大分数。



<strong>示例 1：</strong>

<pre><strong>输入：</strong>nums = [2,-1,0,1,-3,3,-3]
<strong>输出：</strong>6
<strong>解释：</strong>数组重排为 nums = [2,3,1,-1,-3,0,-3] 。
prefix = [2,5,6,5,2,2,-1] ，分数为 6 。
可以证明 6 是能够得到的最大分数。
</pre>

<strong>示例 2：</strong>

<pre><strong>输入：</strong>nums = [-2,-3,0]
<strong>输出：</strong>0
<strong>解释：</strong>不管怎么重排数组得到的分数都是 0 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>-10<sup>6</sup> <= nums[i] <= 10<sup>6</sup></code></li>
</ul>

## 6317.统计美丽子数组数目

[打开力扣](https://leetcode.cn/problems/count-the-number-of-beautiful-subarrays) [我的代码](6317.count_the_number_of_beautiful_subarrays.py)

给你一个下标从 <strong>0</strong>开始的整数数组<code>nums</code>。每次操作中，你可以：

<ul>
	<li>选择两个满足<code>0 <= i, j < nums.length</code>的不同下标<code>i</code>和<code>j</code>。</li>
	<li>选择一个非负整数<code>k</code>，满足 <code>nums[i]</code>和 <code>nums[j]</code>在二进制下的第 <code>k</code>位（下标编号从 <strong>0</strong>开始）是 <code>1</code>。</li>
	<li>将 <code>nums[i]</code>和 <code>nums[j]</code>都减去<code>2<sup>k</sup></code>。</li>
</ul>

如果一个子数组内执行上述操作若干次后，该子数组可以变成一个全为 <code>0</code>的数组，那么我们称它是一个 <strong>美丽</strong>的子数组。

请你返回数组 <code>nums</code>中 <strong>美丽子数组</strong>的数目。

子数组是一个数组中一段连续 <strong>非空</strong>的元素序列。



<strong>示例 1：</strong>

<pre>
<b>输入：</b>nums = [4,3,1,2,4]
<b>输出：</b>2
<b>解释：</b>nums 中有 2 个美丽子数组：[4,<em><strong>3,1,2</strong></em>,4] 和 [<em><strong>4,3,1,2,4</strong></em>] 。
- 按照下述步骤，我们可以将子数组 [3,1,2] 中所有元素变成 0 ：
  - 选择 [<em><strong>3</strong></em>, 1, <em><strong>2</strong></em>] 和 k = 1 。将 2 个数字都减去 2<sup>1</sup> ，子数组变成 [1, 1, 0] 。
  - 选择 [<em><strong>1</strong></em>, <em><strong>1</strong></em>, 0] 和 k = 0 。将 2 个数字都减去 2<sup>0</sup> ，子数组变成 [0, 0, 0] 。
- 按照下述步骤，我们可以将子数组 [4,3,1,2,4] 中所有元素变成 0 ：
  - 选择 [<em><strong>4</strong></em>, 3, 1, 2, <em><strong>4</strong></em>] 和 k = 2 。将 2 个数字都减去 2<sup>2</sup> ，子数组变成 [0, 3, 1, 2, 0] 。
  - 选择 [0, <em><strong>3</strong></em>, <em><strong>1</strong></em>, 2, 0] 和 k = 0 。将 2 个数字都减去 2<sup>0</sup> ，子数组变成 [0, 2, 0, 2, 0] 。
  - 选择 [0, <em><strong>2</strong></em>, 0, <em><strong>2</strong></em>, 0] 和 k = 1 。将 2 个数字都减去 2<sup>1</sup> ，子数组变成 [0, 0, 0, 0, 0] 。
</pre>

<strong>示例 2：</strong>

<pre>
<b>输入：</b>nums = [1,10,4]
<b>输出：</b>0
<b>解释：</b>nums 中没有任何美丽子数组。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>0 <= nums[i] <= 10<sup>6</sup></code></li>
</ul>

## 6318.完成所有任务的最少时间

[打开力扣](https://leetcode.cn/problems/minimum-time-to-complete-all-tasks) [我的代码](6318.minimum_time_to_complete_all_tasks.py)

你有一台电脑，它可以 <strong>同时</strong>运行无数个任务。给你一个二维整数数组<code>tasks</code>，其中<code>tasks[i] = [start<sub>i</sub>, end<sub>i</sub>, duration<sub>i</sub>]</code>表示第<code>i</code>个任务需要在 <strong>闭区间</strong>时间段<code>[start<sub>i</sub>, end<sub>i</sub>]</code>内运行<code>duration<sub>i</sub></code>个整数时间点（但不需要连续）。

当电脑需要运行任务时，你可以打开电脑，如果空闲时，你可以将电脑关闭。

请你返回完成所有任务的情况下，电脑最少需要运行多少秒。



<strong>示例 1：</strong>

<pre><b>输入：</b>tasks = [[2,3,1],[4,5,1],[1,5,2]]
<b>输出：</b>2
<b>解释：</b>
- 第一个任务在闭区间 [2, 2] 运行。
- 第二个任务在闭区间 [5, 5] 运行。
- 第三个任务在闭区间 [2, 2] 和 [5, 5] 运行。
电脑总共运行 2 个整数时间点。
</pre>

<strong>示例 2：</strong>

<pre><b>输入：</b>tasks = [[1,3,2],[2,5,3],[5,6,2]]
<b>输出：</b>4
<b>解释：</b>
- 第一个任务在闭区间 [2, 3] 运行
- 第二个任务在闭区间 [2, 3] 和 [5, 5] 运行。
- 第三个任务在闭区间 [5, 6] 运行。
电脑总共运行 4 个整数时间点。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= tasks.length <= 2000</code></li>
	<li><code>tasks[i].length == 3</code></li>
	<li><code>1 <= start<sub>i</sub>, end<sub>i</sub> <= 2000</code></li>
	<li><code>1 <= duration<sub>i</sub> <= end<sub>i</sub> - start<sub>i</sub> + 1 </code></li>
</ul>
