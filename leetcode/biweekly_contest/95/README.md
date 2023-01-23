# 第 95 场双周赛

> 企业: 力扣

## 2525.根据规则将箱子分类

[打开力扣](https://leetcode.cn/problems/categorize-box-according-to-criteria) [我的代码](2525.categorize_box_according_to_criteria.py)

给你四个整数<code>length</code>，<code>width</code>，<code>height</code>和<code>mass</code>，分别表示一个箱子的三个维度和质量，请你返回一个表示箱子 <strong>类别</strong> 的字符串。

<ul>
	<li>如果满足以下条件，那么箱子是<code>"Bulky"</code>的：

	<ul>
		<li>箱子 <strong>至少有一个</strong> 维度大于等于 <code>10<sup>4</sup></code>。</li>
		<li>或者箱子的 <strong>体积</strong> 大于等于<code>10<sup>9</sup></code>。</li>
	</ul>
	</li>
	<li>如果箱子的质量大于等于<code>100</code>，那么箱子是<code>"Heavy"</code>的。</li>
	<li>如果箱子同时是<code>"Bulky"</code> 和<code>"Heavy"</code>，那么返回类别为<code>"Both"</code>。</li>
	<li>如果箱子既不是<code>"Bulky"</code>，也不是<code>"Heavy"</code>，那么返回类别为<code>"Neither"</code>。</li>
	<li>如果箱子是<code>"Bulky"</code>但不是<code>"Heavy"</code>，那么返回类别为<code>"Bulky"</code>。</li>
	<li>如果箱子是<code>"Heavy"</code>但不是<code>"Bulky"</code>，那么返回类别为<code>"Heavy"</code>。</li>
</ul>

<strong>注意</strong>，箱子的体积等于箱子的长度、宽度和高度的乘积。



<strong>示例 1：</strong>

<pre>
<b>输入：</b>length = 1000, width = 35, height = 700, mass = 300
<b>输出：</b>"Heavy"
<b>解释：</b>
箱子没有任何维度大于等于 10<sup>4 </sup>。
体积为 24500000 <= 10<sup>9 </sup>。所以不能归类为 "Bulky" 。
但是质量 >= 100 ，所以箱子是 "Heavy" 的。
由于箱子不是 "Bulky" 但是是 "Heavy" ，所以我们返回 "Heavy" 。</pre>

<strong>示例 2：</strong>

<pre>
<b>输入：</b>length = 200, width = 50, height = 800, mass = 50
<b>输出：</b>"Neither"
<b>解释：</b>
箱子没有任何维度大于等于 10<sup>4</sup>。
体积为 8 * 10<sup>6</sup> <= 10<sup>9</sup>。所以不能归类为 "Bulky" 。
质量小于 100 ，所以不能归类为 "Heavy" 。
由于不属于上述两者任何一类，所以我们返回 "Neither" 。</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= length, width, height <= 10<sup>5</sup></code></li>
	<li><code>1 <= mass <= 10<sup>3</sup></code></li>
</ul>

## 2526.找到数据流中的连续整数

[打开力扣](https://leetcode.cn/problems/find-consecutive-integers-from-a-data-stream) [我的代码](2526.find_consecutive_integers_from_a_data_stream.py)

给你一个整数数据流，请你实现一个数据结构，检查数据流中最后<code>k</code>个整数是否 <strong>等于</strong> 给定值<code>value</code>。

请你实现<strong>DataStream</strong>类：

<ul>
	<li><code>DataStream(int value, int k)</code>用两个整数 <code>value</code>和 <code>k</code>初始化一个空的整数数据流。</li>
	<li><code>boolean consec(int num)</code>将<code>num</code>添加到整数数据流。如果后 <code>k</code>个整数都等于<code>value</code>，返回<code>true</code>，否则返回<code>false</code>。如果少于<code>k</code>个整数，条件不满足，所以也返回<code>false</code>。</li>
</ul>



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>
["DataStream", "consec", "consec", "consec", "consec"]
[[4, 3], [4], [4], [4], [3]]
<strong>输出：</strong>
[null, false, false, true, false]

<strong>解释：</strong>
DataStream dataStream = new DataStream(4, 3); // value = 4, k = 3
dataStream.consec(4); // 数据流中只有 1 个整数，所以返回 False 。
dataStream.consec(4); // 数据流中只有 2 个整数
                      // 由于 2 小于 k ，返回 False 。
dataStream.consec(4); // 数据流最后 3 个整数都等于 value， 所以返回 True 。
dataStream.consec(3); // 最后 k 个整数分别是 [4,4,3] 。
                      // 由于 3 不等于 value ，返回 False 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= value, num <= 10<sup>9</sup></code></li>
	<li><code>1 <= k <= 10<sup>5</sup></code></li>
	<li>至多调用 <code>consec</code>次数为<code>10<sup>5</sup></code>次。</li>
</ul>

## 2527.查询数组 Xor 美丽值

[打开力扣](https://leetcode.cn/problems/find-xor-beauty-of-array) [我的代码](2527.find_xor_beauty_of_array.py)

给你一个下标从 <strong>0</strong>开始的整数数组<code>nums</code>。

三个下标<code>i</code>，<code>j</code>和<code>k</code>的 <strong>有效值</strong>定义为<code>((nums[i] | nums[j]) &amp; nums[k])</code>。

一个数组的 <strong>xor 美丽值</strong>是数组中所有满足<code>0 <= i, j, k < n</code><strong>的三元组</strong><code>(i, j, k)</code>的 <strong>有效值</strong>的异或结果。

请你返回<code>nums</code>的 xor 美丽值。

<b>注意：</b>

<ul>
	<li><code>val1 | val2</code>是<code>val1</code> 和<code>val2</code>的按位或。</li>
	<li><code>val1 &amp; val2</code>是<code>val1</code> 和<code>val2</code>的按位与。</li>
</ul>



<strong>示例 1：</strong>

<pre>
<b>输入：</b>nums = [1,4]
<b>输出：</b>5
<b>解释：</b>
三元组和它们对应的有效值如下：
- (0,0,0) 有效值为 ((1 | 1) &amp; 1) = 1
- (0,0,1) 有效值为 ((1 | 1) &amp; 4) = 0
- (0,1,0) 有效值为 ((1 | 4) &amp; 1) = 1
- (0,1,1) 有效值为 ((1 | 4) &amp; 4) = 4
- (1,0,0) 有效值为 ((4 | 1) &amp; 1) = 1
- (1,0,1) 有效值为 ((4 | 1) &amp; 4) = 4
- (1,1,0) 有效值为 ((4 | 4) &amp; 1) = 0
- (1,1,1) 有效值为 ((4 | 4) &amp; 4) = 4
数组的 xor 美丽值为所有有效值的按位异或 1 ^ 0 ^ 1 ^ 4 ^ 1 ^ 4 ^ 0 ^ 4 = 5 。</pre>

<strong>示例 2：</strong>

<pre>
<b>输入：</b>nums = [15,45,20,2,34,35,5,44,32,30]
<b>输出：</b>34
<code><span style=""><b>解释：</b>数组的 xor 美丽值为</span> 34 。</code>
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= nums.length<= 10<sup>5</sup></code></li>
	<li><code>1 <= nums[i] <= 10<sup>9</sup></code></li>
</ul>

## 2528.最大化城市的最小供电站数目

[打开力扣](https://leetcode.cn/problems/maximize-the-minimum-powered-city) [我的代码](2528.maximize_the_minimum_powered_city.py)

给你一个下标从 <strong>0</strong>开始长度为 <code>n</code>的整数数组<code>stations</code>，其中<code>stations[i]</code>表示第 <code>i</code>座城市的供电站数目。

每个供电站可以在一定 <strong>范围</strong>内给所有城市提供电力。换句话说，如果给定的范围是<code>r</code>，在城市<code>i</code>处的供电站可以给所有满足<code>|i - j| <= r</code> 且<code>0 <= i, j <= n - 1</code>的城市<code>j</code>供电。

<ul>
	<li><code>|x|</code>表示 <code>x</code>的 <strong>绝对值</strong>。比方说，<code>|7 - 5| = 2</code>，<code>|3 - 10| = 7</code>。</li>
</ul>

一座城市的 <strong>电量</strong>是所有能给它供电的供电站数目。

政府批准了可以额外建造 <code>k</code>座供电站，你需要决定这些供电站分别应该建在哪里，这些供电站与已经存在的供电站有相同的供电范围。

给你两个整数<code>r</code> 和<code>k</code>，如果以最优策略建造额外的发电站，返回所有城市中，最小供电站数目的最大值是多少。

这 <code>k</code>座供电站可以建在多个城市。



<strong>示例 1：</strong>

<pre>
<b>输入：</b>stations = [1,2,4,5,0], r = 1, k = 2
<b>输出：</b>5
<b>解释：</b>
最优方案之一是把 2 座供电站都建在城市 1 。
每座城市的供电站数目分别为 [1,4,4,5,0] 。
- 城市 0 的供电站数目为 1 + 4 = 5 。
- 城市 1 的供电站数目为 1 + 4 + 4 = 9 。
- 城市 2 的供电站数目为 4 + 4 + 5 = 13 。
- 城市 3 的供电站数目为 5 + 4 = 9 。
- 城市 4 的供电站数目为 5 + 0 = 5 。
供电站数目最少是 5 。
无法得到更优解，所以我们返回 5 。
</pre>

<strong>示例 2：</strong>

<pre>
<b>输入：</b>stations = [4,4,4,4], r = 0, k = 3
<b>输出：</b>4
<b>解释：</b>
无论如何安排，总有一座城市的供电站数目是 4 ，所以最优解是 4 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>n == stations.length</code></li>
	<li><code>1 <= n <= 10<sup>5</sup></code></li>
	<li><code>0 <= stations[i] <= 10<sup>5</sup></code></li>
	<li><code>0 <= r<= n - 1</code></li>
	<li><code>0 <= k<= 10<sup>9</sup></code></li>
</ul>
