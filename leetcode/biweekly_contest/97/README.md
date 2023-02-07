# 第 97 场双周赛

> 企业: 力扣 LeetCode

## 2553.分割数组中数字的数位

[打开力扣](https://leetcode.cn/problems/separate-the-digits-in-an-array) [我的代码](2553.separate_the_digits_in_an_array.py)

给你一个正整数数组<code>nums</code>，请你返回一个数组<em></em><code>answer</code> ，你需要将<code>nums</code>中每个整数进行数位分割后，按照<code>nums</code>中出现的<strong>相同顺序</strong>放入答案数组中。

对一个整数进行数位分割，指的是将整数各个数位按原本出现的顺序排列成数组。

<ul>
	<li>比方说，整数<code>10921</code>，分割它的各个数位得到<code>[1,0,9,2,1]</code>。</li>
</ul>



<strong>示例 1：</strong>

<pre><b>输入：</b>nums = [13,25,83,77]
<b>输出：</b>[1,3,2,5,8,3,7,7]
<b>解释：</b>
- 分割 13 得到 [1,3] 。
- 分割 25 得到 [2,5] 。
- 分割 83 得到 [8,3] 。
- 分割 77 得到 [7,7] 。
answer = [1,3,2,5,8,3,7,7] 。answer 中的数字分割结果按照原数字在数组中的相同顺序排列。
</pre>

<strong>示例 2：</strong>

<pre><b>输入：</b>nums = [7,1,3,9]
<b>输出：</b>[7,1,3,9]
<b>解释：</b>nums 中每个整数的分割是它自己。
answer = [7,1,3,9] 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length <= 1000</code></li>
	<li><code>1 <= nums[i] <= 10<sup>5</sup></code></li>
</ul>

## 2554.从一个范围内选择最多整数 I

[打开力扣](https://leetcode.cn/problems/maximum-number-of-integers-to-choose-from-a-range-i) [我的代码](2554.maximum_number_of_integers_to_choose_from_a_range_i.py)

给你一个整数数组<code>banned</code>和两个整数<code>n</code> 和<code>maxSum</code>。你需要按照以下规则选择一些整数：

<ul>
	<li>被选择整数的范围是<code>[1, n]</code>。</li>
	<li>每个整数 <strong>至多</strong>选择 <strong>一次</strong>。</li>
	<li>被选择整数不能在数组<code>banned</code>中。</li>
	<li>被选择整数的和不超过<code>maxSum</code>。</li>
</ul>

请你返回按照上述规则 <strong>最多</strong>可以选择的整数数目。



<strong>示例 1：</strong>

<pre><b>输入：</b>banned = [1,6,5], n = 5, maxSum = 6
<b>输出：</b>2
<b>解释：</b>你可以选择整数 2 和 4 。
2 和 4 在范围 [1, 5] 内，且它们都不在 banned 中，它们的和是 6 ，没有超过 maxSum 。
</pre>

<strong>示例 2：</strong>

<pre><b>输入：</b>banned = [1,2,3,4,5,6,7], n = 8, maxSum = 1
<b>输出：</b>0
<b>解释：</b>按照上述规则无法选择任何整数。
</pre>

<strong>示例 3：</strong>

<pre><b>输入：</b>banned = [11], n = 7, maxSum = 50
<b>输出：</b>7
<b>解释：</b>你可以选择整数 1, 2, 3, 4, 5, 6 和 7 。
它们都在范围 [1, 7] 中，且都没出现在 banned 中，它们的和是 28 ，没有超过 maxSum 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= banned.length <= 10<sup>4</sup></code></li>
	<li><code>1 <= banned[i], n <= 10<sup>4</sup></code></li>
	<li><code>1 <= maxSum <= 10<sup>9</sup></code></li>
</ul>

## 2555.两个线段获得的最多奖品

[打开力扣](https://leetcode.cn/problems/maximize-win-from-two-segments) [我的代码](2555.maximize_win_from_two_segments.py)

在 <strong>X轴</strong>上有一些奖品。给你一个整数数组<code>prizePositions</code>，它按照 <strong>非递减</strong>顺序排列，其中<code>prizePositions[i]</code>是第<code>i</code>件奖品的位置。数轴上一个位置可能会有多件奖品。再给你一个整数<code>k</code>。

你可以选择两个端点为整数的线段。每个线段的长度都必须是 <code>k</code>。你可以获得位置在任一线段上的所有奖品（包括线段的两个端点）。注意，两个线段可能会有相交。

<ul>
	<li>比方说<code>k = 2</code>，你可以选择线段<code>[1, 3]</code> 和<code>[2, 4]</code>，你可以获得满足<code>1 <= prizePositions[i] <= 3</code> 或者<code>2 <= prizePositions[i] <= 4</code>的所有奖品 i 。</li>
</ul>

请你返回在选择两个最优线段的前提下，可以获得的 <strong>最多</strong>奖品数目。



<strong>示例 1：</strong>

<pre>
<b>输入：</b>prizePositions = [1,1,2,2,3,3,5], k = 2
<b>输出：</b>7
<b>解释：</b>这个例子中，你可以选择线段 [1, 3] 和 [3, 5] ，获得 7 个奖品。
</pre>

<strong>示例 2：</strong>

<pre>
<b>输入：</b>prizePositions = [1,2,3,4], k = 0
<b>输出：</b>2
<b>解释：</b>这个例子中，一个选择是选择线段 <code>[3, 3]</code> 和 <code>[4, 4] ，获得 2 个奖品。</code>
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= prizePositions.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= prizePositions[i] <= 10<sup>9</sup></code></li>
	<li><code>0 <= k <= 10<sup>9</sup> </code></li>
	<li><code>prizePositions</code>有序非递减。</li>
</ul>

## 2556.二进制矩阵中翻转最多一次使路径不连通

[打开力扣](https://leetcode.cn/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip) [我的代码](2556.disconnect_path_in_a_binary_matrix_by_at_most_one_flip.py)

给你一个下标从 <strong>0</strong>开始的<code>m x n</code><strong>二进制</strong> 矩阵<code>grid</code>。你可以从一个格子<code>(row, col)</code>移动到格子<code>(row + 1, col)</code>或者<code>(row, col + 1)</code>，前提是前往的格子值为 <code>1</code>。如果从<code>(0, 0)</code>到<code>(m - 1, n - 1)</code>没有任何路径，我们称该矩阵是<strong>不连通</strong>的。

你可以翻转 <strong>最多一个</strong>格子的值（也可以不翻转）。你 <strong>不能翻转</strong>格子<code>(0, 0)</code> 和<code>(m - 1, n - 1)</code>。

如果可以使矩阵不连通，请你返回<code>true</code>，否则返回<em></em><code>false</code><em></em>。

<strong>注意</strong>，翻转一个格子的值，可以使它的值从<code>0</code>变<code>1</code>，或从<code>1</code>变<code>0</code>。



<strong>示例 1：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/12/07/yetgrid2drawio.png" style="width: 441px; height: 151px;" />

<pre>
<b>输入：</b>grid = [[1,1,1],[1,0,0],[1,1,1]]
<strong>输出：</strong>true
<b>解释：</b>按照上图所示我们翻转蓝色格子里的值，翻转后从 (0, 0) 到 (2, 2) 没有路径。
</pre>

<strong>示例 2：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/12/07/yetgrid3drawio.png" />

<pre>
<b>输入：</b>grid = [[1,1,1],[1,0,1],[1,1,1]]
<b>输出：</b>false
<b>解释：</b>无法翻转至多一个格子，使 (0, 0) 到 (2, 2) 没有路径。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 <= m, n <= 1000</code></li>
	<li><code>1 <= m * n <= 10<sup>5</sup></code></li>
	<li><code>grid[0][0] == grid[m - 1][n - 1] == 1</code></li>
</ul>
