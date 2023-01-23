# 第 327 场周赛

> 企业: 力扣

## 6283.正整数和负整数的最大计数

[打开力扣](https://leetcode.cn/problems/maximum-count-of-positive-integer-and-negative-integer) [我的代码](6283.maximum_count_of_positive_integer_and_negative_integer.py)

给你一个按 <strong>非递减顺序</strong> 排列的数组 <code>nums</code> ，返回正整数数目和负整数数目中的最大值。

<ul>
	<li>换句话讲，如果 <code>nums</code> 中正整数的数目是 <code>pos</code> ，而负整数的数目是 <code>neg</code> ，返回 <code>pos</code> 和 <code>neg</code>二者中的最大值。</li>
</ul>

<strong>注意：</strong><code>0</code> 既不是正整数也不是负整数。



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>nums = [-2,-1,-1,1,2,3]
<strong>输出：</strong>3
<strong>解释：</strong>共有 3 个正整数和 3 个负整数。计数得到的最大值是 3 。
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>nums = [-3,-2,-1,0,0,1,2]
<strong>输出：</strong>3
<strong>解释：</strong>共有 2 个正整数和 3 个负整数。计数得到的最大值是 3 。
</pre>

<strong>示例 3：</strong>

<pre>
<strong>输入：</strong>nums = [5,20,66,1314]
<strong>输出：</strong>4
<strong>解释：</strong>共有 4 个正整数和 0 个负整数。计数得到的最大值是 4 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length <= 2000</code></li>
	<li><code>-2000 <= nums[i] <= 2000</code></li>
	<li><code>nums</code> 按 <strong>非递减顺序</strong> 排列。</li>
</ul>

## 6285.执行 K 次操作后的最大分数

[打开力扣](https://leetcode.cn/problems/maximal-score-after-applying-k-operations) [我的代码](6285.maximal_score_after_applying_k_operations.py)

给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> 和一个整数 <code>k</code> 。你的 <strong>起始分数</strong> 为 <code>0</code> 。

在一步 <strong>操作</strong> 中：

<ol>
	<li>选出一个满足 <code>0 <= i < nums.length</code> 的下标 <code>i</code> ，</li>
	<li>将你的 <strong>分数</strong> 增加 <code>nums[i]</code> ，并且</li>
	<li>将 <code>nums[i]</code> 替换为 <code>ceil(nums[i] / 3)</code> 。</li>
</ol>

返回在 <strong>恰好</strong> 执行 <code>k</code> 次操作后，你可能获得的最大分数。

向上取整函数 <code>ceil(val)</code> 的结果是大于或等于 <code>val</code> 的最小整数。



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>nums = [10,10,10,10,10], k = 5
<strong>输出：</strong>50
<strong>解释：</strong>对数组中每个元素执行一次操作。最后分数是 10 + 10 + 10 + 10 + 10 = 50 。
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>nums = [1,10,3,3,3], k = 3
<strong>输出：</strong>17
<strong>解释：</strong>可以执行下述操作：
第 1 步操作：选中 i = 1 ，nums 变为 [1,<em><strong>4</strong></em>,3,3,3] 。分数增加 10 。
第 2 步操作：选中 i = 1 ，nums 变为 [1,<em><strong>2</strong></em>,3,3,3] 。分数增加 4 。
第 3 步操作：选中 i = 2 ，nums 变为 [1,1,<em><strong>1</strong></em>,3,3] 。分数增加 3 。
最后分数是 10 + 4 + 3 = 17 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length, k <= 10<sup>5</sup></code></li>
	<li><code>1 <= nums[i] <= 10<sup>9</sup></code></li>
</ul>

## 6284.使字符串总不同字符的数目相等

[打开力扣](https://leetcode.cn/problems/make-number-of-distinct-characters-equal) [我的代码](6284.make_number_of_distinct_characters_equal.py)

给你两个下标从 <strong>0</strong> 开始的字符串 <code>word1</code> 和 <code>word2</code> 。

一次 <strong>移动</strong> 由以下两个步骤组成：

<ul>
	<li>选中两个下标<code>i</code> 和 <code>j</code> ，分别满足 <code>0 <= i < word1.length</code> 和 <code>0 <= j < word2.length</code> ，</li>
	<li>交换 <code>word1[i]</code> 和 <code>word2[j]</code> 。</li>
</ul>

如果可以通过 <strong>恰好一次</strong> 移动，使 <code>word1</code> 和 <code>word2</code> 中不同字符的数目相等，则返回 <code>true</code> ；否则，返回 <code>false</code> 。



<strong>示例 1：</strong>

<pre><strong>输入：</strong>word1 = "ac", word2 = "b"
<strong>输出：</strong>false
<strong>解释：</strong>交换任何一组下标都会导致第一个字符串中有 2 个不同的字符，而在第二个字符串中只有 1 个不同字符。
</pre>

<strong>示例 2：</strong>

<pre><strong>输入：</strong>word1 = "abcc", word2 = "aab"
<strong>输出：</strong>true
<strong>解释：</strong>交换第一个字符串的下标 2 和第二个字符串的下标 0 。之后得到 word1 = "abac" 和 word2 = "cab" ，各有 3 个不同字符。
</pre>

<strong>示例 3：</strong>

<pre><strong>输入：</strong>word1 = "abcde", word2 = "fghij"
<strong>输出：</strong>true
<strong>解释：</strong>无论交换哪一组下标，两个字符串中都会有 5 个不同字符。</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= word1.length, word2.length <= 10<sup>5</sup></code></li>
	<li><code>word1</code> 和 <code>word2</code> 仅由小写英文字母组成。</li>
</ul>

## 6306.过桥的时间

[打开力扣](https://leetcode.cn/problems/time-to-cross-a-bridge) [我的代码](6306.time_to_cross_a_bridge.py)

共有 <code>k</code> 位工人计划将 <code>n</code> 个箱子从旧仓库移动到新仓库。给你两个整数 <code>n</code> 和 <code>k</code>，以及一个二维整数数组 <code>time</code> ，数组的大小为 <code>k x 4</code> ，其中 <code>time[i] = [leftToRight<sub>i</sub>, pickOld<sub>i</sub>, rightToLeft<sub>i</sub>, putNew<sub>i</sub>]</code> 。

一条河将两座仓库分隔，只能通过一座桥通行。旧仓库位于河的右岸，新仓库在河的左岸。开始时，所有 <code>k</code> 位工人都在桥的左侧等待。为了移动这些箱子，第 <code>i</code> 位工人（下标从 <strong>0</strong> 开始）可以：

<ul>
	<li>从左岸（新仓库）跨过桥到右岸（旧仓库），用时 <code>leftToRight<sub>i</sub></code> 分钟。</li>
	<li>从旧仓库选择一个箱子，并返回到桥边，用时 <code>pickOld<sub>i</sub></code> 分钟。不同工人可以同时搬起所选的箱子。</li>
	<li>从右岸（旧仓库）跨过桥到左岸（新仓库），用时 <code>rightToLeft<sub>i</sub></code> 分钟。</li>
	<li>将箱子放入新仓库，并返回到桥边，用时 <code>putNew<sub>i</sub></code> 分钟。不同工人可以同时放下所选的箱子。</li>
</ul>

如果满足下面任一条件，则认为工人 <code>i</code> 的 <strong>效率低于</strong> 工人 <code>j</code> ：

<ul>
	<li><code>leftToRight<sub>i</sub> + rightToLeft<sub>i</sub> > leftToRight<sub>j</sub> + rightToLeft<sub>j</sub></code></li>
	<li><code>leftToRight<sub>i</sub> + rightToLeft<sub>i</sub> == leftToRight<sub>j</sub> + rightToLeft<sub>j</sub></code> 且 <code>i > j</code></li>
</ul>

工人通过桥时需要遵循以下规则：

<ul>
	<li>如果工人 <code>x</code> 到达桥边时，工人 <code>y</code> 正在过桥，那么工人 <code>x</code> 需要在桥边等待。</li>
	<li>如果没有正在过桥的工人，那么在桥右边等待的工人可以先过桥。如果同时有多个工人在右边等待，那么 <strong>效率最低</strong> 的工人会先过桥。</li>
	<li>如果没有正在过桥的工人，且桥右边也没有在等待的工人，同时旧仓库还剩下至少一个箱子需要搬运，此时在桥左边的工人可以过桥。如果同时有多个工人在左边等待，那么 <strong>效率最低</strong> 的工人会先过桥。</li>
</ul>

所有 <code>n</code> 个盒子都需要放入新仓库，<span class="text-only" data-eleid="8" style="white-space: pre;">请你返回最后一个搬运箱子的工人 </span><strong><span class="text-only" data-eleid="9" style="white-space: pre;">到达河左岸</span></strong><span class="text-only" data-eleid="10" style="white-space: pre;"> 的时间。</span>



<strong class="example">示例 1：</strong>

<pre>
<strong>输入：</strong>n = 1, k = 3, time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]]
<strong>输出：</strong>6
<strong>解释：</strong>
从 0 到 1 ：工人 2 从左岸过桥到达右岸。
从 1 到 2 ：工人 2 从旧仓库搬起一个箱子。
从 2 到 6 ：工人 2 从右岸过桥到达左岸。
从 6 到 7 ：工人 2 将箱子放入新仓库。
整个过程在 7 分钟后结束。因为问题关注的是最后一个工人到达左岸的时间，所以返回 6 。
</pre>

<strong class="example">示例 2：</strong>

<pre>
<strong>输入：</strong>n = 3, k = 2, time = [[1,9,1,8],[10,10,10,10]]
<strong>输出：</strong>50
<strong>解释：</strong>
从 0 到 10 ：工人 1 从左岸过桥到达右岸。
从 10 到 20 ：工人 1 从旧仓库搬起一个箱子。
从 10 到 11 ：工人 0 从左岸过桥到达右岸。
从 11 到 20 ：工人 0 从旧仓库搬起一个箱子。
从 20 到 30 ：工人 1 从右岸过桥到达左岸。
从 30 到 40 ：工人 1 将箱子放入新仓库。
从 30 到 31 ：工人 0 从右岸过桥到达左岸。
从 31 到 39 ：工人 0 将箱子放入新仓库。
从 39 到 40 ：工人 0 从左岸过桥到达右岸。
从 40 到 49 ：工人 0 从旧仓库搬起一个箱子。
从 49 到 50 ：工人 0 从右岸过桥到达左岸。
从 50 到 58 ：工人 0 将箱子放入新仓库。
整个过程在 58 分钟后结束。因为问题关注的是最后一个工人到达左岸的时间，所以返回 50 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= n, k <= 10<sup>4</sup></code></li>
	<li><code>time.length == k</code></li>
	<li><code>time[i].length == 4</code></li>
	<li><code>1 <= leftToRight<sub>i</sub>, pickOld<sub>i</sub>, rightToLeft<sub>i</sub>, putNew<sub>i</sub> <= 1000</code></li>
</ul>
