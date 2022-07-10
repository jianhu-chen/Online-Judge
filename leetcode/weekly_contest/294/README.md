# 第 294 场周赛

> 企业: 普渡机器人

## 2278.字母在字符串中的百分比

[打开力扣](https://leetcode.cn/problems/percentage-of-letter-in-string) [我的代码](2278.percentage_of_letter_in_string.py)

给你一个字符串 <code>s</code> 和一个字符 <code>letter</code> ，返回在 <code>s</code> 中等于<code>letter</code>字符所占的 <strong>百分比</strong> ，向下取整到最接近的百分比。



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>s = "foobar", letter = "o"
<strong>输出：</strong>33
<strong>解释：</strong>
等于字母 'o' 的字符在 s 中占到的百分比是 2 / 6 * 100% = 33% ，向下取整，所以返回 33 。
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>s = "jjjj", letter = "k"
<strong>输出：</strong>0
<strong>解释：</strong>
等于字母 'k' 的字符在 s 中占到的百分比是 0% ，所以返回 0 。</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= s.length <= 100</code></li>
	<li><code>s</code> 由小写英文字母组成</li>
	<li><code>letter</code> 是一个小写英文字母</li>
</ul>

## 2279.装满石头的背包的最大数量

[打开力扣](https://leetcode.cn/problems/maximum-bags-with-full-capacity-of-rocks) [我的代码](2279.maximum_bags_with_full_capacity_of_rocks.py)

现有编号从<code>0</code> 到 <code>n - 1</code> 的 <code>n</code> 个背包。给你两个下标从 <strong>0</strong> 开始的整数数组 <code>capacity</code> 和 <code>rocks</code> 。第 <code>i</code> 个背包最大可以装 <code>capacity[i]</code> 块石头，当前已经装了 <code>rocks[i]</code> 块石头。另给你一个整数 <code>additionalRocks</code> ，表示<span class="text-only" data-eleid="10" style="white-space: pre;">你可以放置的额外石头数量，石头可以往 </span><strong><span class="text-only" data-eleid="11" style="white-space: pre;">任意</span></strong><span class="text-only" data-eleid="12" style="white-space: pre;"> 背包中放置。</span>

请你将额外的石头放入一些背包中，并返回放置后装满石头的背包的 <strong>最大 </strong>数量<em>。</em>



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2
<strong>输出：</strong>3
<strong>解释：</strong>
1 块石头放入背包 0 ，1 块石头放入背包 1 。
每个背包中的石头总数是 [2,3,4,4] 。
背包 0 、背包 1 和 背包 2 都装满石头。
总计 3 个背包装满石头，所以返回 3 。
可以证明不存在超过 3 个背包装满石头的情况。
注意，可能存在其他放置石头的方案同样能够得到 3 这个结果。
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>capacity = [10,2,2], rocks = [2,2,0], additionalRocks = 100
<strong>输出：</strong>3
<strong>解释：</strong>
8 块石头放入背包 0 ，2 块石头放入背包 2 。
每个背包中的石头总数是 [10,2,2] 。
背包 0 、背包 1 和背包 2 都装满石头。
总计 3 个背包装满石头，所以返回 3 。
可以证明不存在超过 3 个背包装满石头的情况。
注意，不必用完所有的额外石头。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>n == capacity.length == rocks.length</code></li>
	<li><code>1 <= n <= 5 * 10<sup>4</sup></code></li>
	<li><code>1 <= capacity[i] <= 10<sup>9</sup></code></li>
	<li><code>0 <= rocks[i] <= capacity[i]</code></li>
	<li><code>1 <= additionalRocks <= 10<sup>9</sup></code></li>
</ul>

## 2280.表示一个折线图的最少线段数

[打开力扣](https://leetcode.cn/problems/minimum-lines-to-represent-a-line-chart) [我的代码](2280.minimum_lines_to_represent_a_line_chart.py)

给你一个二维整数数组<code>stockPrices</code> ，其中<code>stockPrices[i] = [day<sub>i</sub>, price<sub>i</sub>]</code>表示股票在<code>day<sub>i</sub></code>的价格为<code>price<sub>i</sub></code>。<strong>折线图</strong>是一个二维平面上的若干个点组成的图，横坐标表示日期，纵坐标表示价格，折线图由相邻的点连接而成。比方说下图是一个例子：
<img alt="" src="https://assets.leetcode.com/uploads/2022/03/30/1920px-pushkin_population_historysvg.png" style="width: 500px; height: 313px;">
请你返回要表示一个折线图所需要的 <strong>最少线段数</strong>。



<strong>示例 1：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/03/30/ex0.png" style="width: 400px; height: 400px;">

<pre><b>输入：</b>stockPrices = [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]
<b>输出：</b>3
<strong>解释：</strong>
上图为输入对应的图，横坐标表示日期，纵坐标表示价格。
以下 3 个线段可以表示折线图：
- 线段 1 （红色）从 (1,7) 到 (4,4) ，经过 (1,7) ，(2,6) ，(3,5) 和 (4,4) 。
- 线段 2 （蓝色）从 (4,4) 到 (5,4) 。
- 线段 3 （绿色）从 (5,4) 到 (8,1) ，经过 (5,4) ，(6,3) ，(7,2) 和 (8,1) 。
可以证明，无法用少于 3 条线段表示这个折线图。
</pre>

<strong>示例 2：</strong>

<img alt="" src="https://assets.leetcode.com/uploads/2022/03/30/ex1.png" style="width: 325px; height: 325px;">

<pre><b>输入：</b>stockPrices = [[3,4],[1,2],[7,8],[2,3]]
<b>输出：</b>1
<strong>解释：</strong>
如上图所示，折线图可以用一条线段表示。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= stockPrices.length <= 10<sup>5</sup></code></li>
	<li><code>stockPrices[i].length == 2</code></li>
	<li><code>1 <= day<sub>i</sub>, price<sub>i</sub> <= 10<sup>9</sup></code></li>
	<li>所有<code>day<sub>i</sub></code><strong>互不相同</strong>。</li>
</ul>

## 2281.巫师的总力量和

[打开力扣](https://leetcode.cn/problems/sum-of-total-strength-of-wizards) [我的代码](2281.sum_of_total_strength_of_wizards.py)

作为国王的统治者，你有一支巫师军队听你指挥。

给你一个下标从 <strong>0</strong>开始的整数数组<code>strength</code>，其中<code>strength[i]</code>表示第<code>i</code>位巫师的力量值。对于连续的一组巫师（也就是这些巫师的力量值是<code>strength</code>的<strong>子数组</strong>），<strong>总力量</strong>定义为以下两个值的<strong>乘积</strong>：

<ul>
	<li>巫师中 <strong>最弱</strong>的能力值。</li>
	<li>组中所有巫师的个人力量值 <strong>之和</strong>。</li>
</ul>

请你返回 <strong>所有</strong>巫师组的 <strong>总</strong>力量之和。由于答案可能很大，请将答案对<code>10<sup>9</sup> + 7</code><strong>取余</strong>后返回。

<strong>子数组</strong>是一个数组里 <strong>非空</strong>连续子序列。



<strong>示例 1：</strong>

<pre><b>输入：</b>strength = [1,3,1,2]
<b>输出：</b>44
<b>解释：</b>以下是所有连续巫师组：
- [<em><strong>1</strong></em>,3,1,2] 中 [1] ，总力量值为 min([1]) * sum([1]) = 1 * 1 = 1
- [1,<em><strong>3</strong></em>,1,2] 中 [3] ，总力量值为 min([3]) * sum([3]) = 3 * 3 = 9
- [1,3,<em><strong>1</strong></em>,2] 中 [1] ，总力量值为 min([1]) * sum([1]) = 1 * 1 = 1
- [1,3,1,<em><strong>2</strong></em>] 中 [2] ，总力量值为 min([2]) * sum([2]) = 2 * 2 = 4
- [<em><strong>1,3</strong></em>,1,2] 中 [1,3] ，总力量值为 min([1,3]) * sum([1,3]) = 1 * 4 = 4
- [1,<em><strong>3,1</strong></em>,2] 中 [3,1] ，总力量值为 min([3,1]) * sum([3,1]) = 1 * 4 = 4
- [1,3,<em><strong>1,2</strong></em>] 中 [1,2] ，总力量值为 min([1,2]) * sum([1,2]) = 1 * 3 = 3
- [<em><strong>1,3,1</strong></em>,2] 中 [1,3,1] ，总力量值为 min([1,3,1]) * sum([1,3,1]) = 1 * 5 = 5
- [1,<em><strong>3,1,2</strong></em>] 中 [3,1,2] ，总力量值为 min([3,1,2]) * sum([3,1,2]) = 1 * 6 = 6
- [<em><strong>1,3,1,2</strong></em>] 中 [1,3,1,2] ，总力量值为 min([1,3,1,2]) * sum([1,3,1,2]) = 1 * 7 = 7
所有力量值之和为 1 + 9 + 1 + 4 + 4 + 4 + 3 + 5 + 6 + 7 = 44 。
</pre>

<strong>示例 2：</strong>

<pre><b>输入：</b>strength = [5,4,6]
<b>输出：</b>213
<b>解释：</b>以下是所有连续巫师组：
- [<em><strong>5</strong></em>,4,6] 中 [5] ，总力量值为 min([5]) * sum([5]) = 5 * 5 = 25
- [5,<em><strong>4</strong></em>,6] 中 [4] ，总力量值为 min([4]) * sum([4]) = 4 * 4 = 16
- [5,4,<em><strong>6</strong></em>] 中 [6] ，总力量值为 min([6]) * sum([6]) = 6 * 6 = 36
- [<em><strong>5,4</strong></em>,6] 中 [5,4] ，总力量值为 min([5,4]) * sum([5,4]) = 4 * 9 = 36
- [5,<em><strong>4,6</strong></em>] 中 [4,6] ，总力量值为 min([4,6]) * sum([4,6]) = 4 * 10 = 40
- [<em><strong>5,4,6</strong></em>] 中 [5,4,6] ，总力量值为 min([5,4,6]) * sum([5,4,6]) = 4 * 15 = 60
所有力量值之和为 25 + 16 + 36 + 36 + 40 + 60 = 213 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= strength.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= strength[i] <= 10<sup>9</sup></code></li>
</ul>
