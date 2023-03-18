# 第 100 场双周赛

> 企业: 力扣 LeetCode

## 6323.将钱分给最多的儿童

[打开力扣](https://leetcode.cn/problems/distribute-money-to-maximum-children) [我的代码](6323.distribute_money_to_maximum_children.py)

给你一个整数<code>money</code>，表示你总共有的钱数（单位为美元）和另一个整数<code>children</code>，表示你要将钱分配给多少个儿童。

你需要按照如下规则分配：

<ul>
	<li>所有的钱都必须被分配。</li>
	<li>每个儿童至少获得<code>1</code>美元。</li>
	<li>没有人获得 <code>4</code>美元。</li>
</ul>

请你按照上述规则分配金钱，并返回 <strong>最多</strong>有多少个儿童获得 <strong>恰好</strong><em></em><code>8</code>美元。如果没有任何分配方案，返回<code>-1</code>。



<strong>示例 1：</strong>

<pre><b>输入：</b>money = 20, children = 3
<b>输出：</b>1
<b>解释：</b>
最多获得 8 美元的儿童数为 1 。一种分配方案为：
- 给第一个儿童分配 8 美元。
- 给第二个儿童分配 9 美元。
- 给第三个儿童分配 3 美元。
没有分配方案能让获得 8 美元的儿童数超过 1 。
</pre>

<strong>示例 2：</strong>

<pre><b>输入：</b>money = 16, children = 2
<b>输出：</b>2
<b>解释：</b>每个儿童都可以获得 8 美元。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= money <= 200</code></li>
	<li><code>2 <= children <= 30</code></li>
</ul>

## 6324.最大化数组的伟大值

[打开力扣](https://leetcode.cn/problems/maximize-greatness-of-an-array) [我的代码](6324.maximize_greatness_of_an_array.py)

给你一个下标从 0 开始的整数数组<code>nums</code>。你需要将<code>nums</code>重新排列成一个新的数组<code>perm</code>。

定义 <code>nums</code>的 <strong>伟大值</strong>为满足<code>0 <= i < nums.length</code>且<code>perm[i] > nums[i]</code>的下标数目。

请你返回重新排列 <code>nums</code>后的 <strong>最大</strong>伟大值。



<strong>示例 1：</strong>

<pre><b>输入：</b>nums = [1,3,5,2,1,3,1]
<b>输出：</b>4
<b>解释：</b>一个最优安排方案为 perm = [2,5,1,3,3,1,1] 。
在下标为 0, 1, 3 和 4 处，都有 perm[i] > nums[i] 。因此我们返回 4 。</pre>

<strong>示例 2：</strong>

<pre><b>输入：</b>nums = [1,2,3,4]
<b>输出：</b>3
<b>解释：</b>最优排列为 [2,3,4,1] 。
在下标为 0, 1 和 2 处，都有 perm[i] > nums[i] 。因此我们返回 3 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>0 <= nums[i] <= 10<sup>9</sup></code></li>
</ul>

## 6351.标记所有元素后数组的分数

[打开力扣](https://leetcode.cn/problems/find-score-of-an-array-after-marking-all-elements) [我的代码](6351.find_score_of_an_array_after_marking_all_elements.py)

给你一个数组<code>nums</code>，它包含若干正整数。

一开始分数<code>score = 0</code>，请你按照下面算法求出最后分数：

<ul>
	<li>从数组中选择最小且没有被标记的整数。如果有相等元素，选择下标最小的一个。</li>
	<li>将选中的整数加到<code>score</code>中。</li>
	<li>标记 <strong>被选中元素</strong>，如果有相邻元素，则同时标记<strong>与它相邻的两个元素</strong>。</li>
	<li>重复此过程直到数组中所有元素都被标记。</li>
</ul>

请你返回执行上述算法后最后的分数。



<strong>示例 1：</strong>

<pre><b>输入：</b>nums = [2,1,3,4,5,2]
<b>输出：</b>7
<b>解释：</b>我们按照如下步骤标记元素：
- 1 是最小未标记元素，所以标记它和相邻两个元素：[<em><strong>2</strong></em>,<em><strong>1</strong></em>,<em><strong>3</strong></em>,4,5,2] 。
- 2 是最小未标记元素，所以标记它和左边相邻元素：[<em><strong>2</strong></em>,<em><strong>1</strong></em>,<em><strong>3</strong></em>,4,<em><strong>5</strong></em>,<em><strong>2</strong></em>] 。
- 4 是仅剩唯一未标记的元素，所以我们标记它：[<em><strong>2</strong></em>,<em><strong>1</strong></em>,<em><strong>3</strong></em>,<em><strong>4</strong></em>,<em><strong>5</strong></em>,<em><strong>2</strong></em>] 。
总得分为 1 + 2 + 4 = 7 。
</pre>

<strong>示例 2：</strong>

<pre><b>输入：</b>nums = [2,3,5,1,3,2]
<b>输出：</b>5
<b>解释：</b>我们按照如下步骤标记元素：
- 1 是最小未标记元素，所以标记它和相邻两个元素：[2,3,<em><strong>5</strong></em>,<em><strong>1</strong></em>,<em><strong>3</strong></em>,2] 。
- 2 是最小未标记元素，由于有两个 2 ，我们选择最左边的一个 2 ，也就是下标为 0 处的 2 ，以及它右边相邻的元素：[<em><strong>2</strong></em>,<em><strong>3</strong></em>,<em><strong>5</strong></em>,<em><strong>1</strong></em>,<em><strong>3</strong></em>,2] 。
- 2 是仅剩唯一未标记的元素，所以我们标记它：[<em><strong>2</strong></em>,<em><strong>3</strong></em>,<em><strong>5</strong></em>,<em><strong>1</strong></em>,<em><strong>3</strong></em>,<em><strong>2</strong></em>] 。
总得分为 1 + 2 + 2 = 5 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= nums[i] <= 10<sup>6</sup></code></li>
</ul>

## 6325.修车的最少时间

[打开力扣](https://leetcode.cn/problems/minimum-time-to-repair-cars) [我的代码](6325.minimum_time_to_repair_cars.py)

给你一个整数数组<code>ranks</code>，表示一些机械工的 <strong>能力值</strong>。<code>ranks<sub>i</sub></code> 是第 <code>i</code> 位机械工的能力值。能力值为<code>r</code>的机械工可以在<code>r * n<sup>2</sup></code>分钟内修好<code>n</code>辆车。

同时给你一个整数<code>cars</code>，表示总共需要修理的汽车数目。

请你返回修理所有汽车<strong>最少</strong>需要多少时间。

<strong>注意：</strong>所有机械工可以同时修理汽车。



<strong>示例 1：</strong>

<pre>
<b>输入：</b>ranks = [4,2,3,1], cars = 10
<b>输出：</b>16
<b>解释：</b>
- 第一位机械工修 2 辆车，需要 4 * 2 * 2 = 16 分钟。
- 第二位机械工修 2 辆车，需要 2 * 2 * 2 = 8 分钟。
- 第三位机械工修 2 辆车，需要 3 * 2 * 2 = 12 分钟。
- 第四位机械工修 4 辆车，需要 1 * 4 * 4 = 16 分钟。
16 分钟是修理完所有车需要的最少时间。
</pre>

<strong>示例 2：</strong>

<pre>
<b>输入：</b>ranks = [5,1,8], cars = 6
<b>输出：</b>16
<b>解释：</b>
- 第一位机械工修 1 辆车，需要 5 * 1 * 1 = 5 分钟。
- 第二位机械工修 4 辆车，需要 1 * 4 * 4 = 16 分钟。
- 第三位机械工修 1 辆车，需要 8 * 1 * 1 = 8 分钟。
16 分钟时修理完所有车需要的最少时间。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= ranks.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= ranks[i] <= 100</code></li>
	<li><code>1 <= cars <= 10<sup>6</sup></code></li>
</ul>
