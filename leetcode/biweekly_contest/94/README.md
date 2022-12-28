# 第 94 场双周赛

> 企业: 恒生电子

## 2511.最多可以摧毁的敌人城堡数目

[打开力扣](https://leetcode.cn/problems/maximum-enemy-forts-that-can-be-captured) [我的代码](2511.maximum_enemy_forts_that_can_be_captured.py)

给你一个长度为 <code>n</code>，下标从 <strong>0</strong>开始的整数数组<code>forts</code>，表示一些城堡。<code>forts[i]</code> 可以是<code>-1</code>，<code>0</code>或者<code>1</code>，其中：

<ul>
	<li><code>-1</code>表示第<code>i</code>个位置 <strong>没有</strong>城堡。</li>
	<li><code>0</code>表示第<code>i</code>个位置有一个 <strong>敌人</strong>的城堡。</li>
	<li><code>1</code>表示第<code>i</code>个位置有一个你控制的城堡。</li>
</ul>

现在，你需要决定，将你的军队从某个你控制的城堡位置<code>i</code>移动到一个空的位置<code>j</code>，满足：

<ul>
	<li><code>0 <= i, j <= n - 1</code></li>
	<li>军队经过的位置 <strong>只有</strong>敌人的城堡。正式的，对于所有<code>min(i,j) < k < max(i,j)</code>的<code>k</code>，都满足<code>forts[k] == 0</code>。</li>
</ul>

当军队移动时，所有途中经过的敌人城堡都会被 <strong>摧毁</strong> 。

请你返回 <strong>最多</strong>可以摧毁的敌人城堡数目。如果 <strong>无法</strong>移动你的军队，或者没有你控制的城堡，请返回 <code>0</code>。



<strong>示例 1：</strong>

<pre><b>输入：</b>forts = [1,0,0,-1,0,0,0,0,1]
<b>输出：</b>4
<strong>解释：</strong>
- 将军队从位置 0 移动到位置 3 ，摧毁 2 个敌人城堡，位置分别在 1 和 2 。
- 将军队从位置 8 移动到位置 3 ，摧毁 4 个敌人城堡。
4 是最多可以摧毁的敌人城堡数目，所以我们返回 4 。
</pre>

<strong>示例 2：</strong>

<pre><b>输入：</b>forts = [0,0,1,-1]
<b>输出：</b>0
<b>解释：</b>由于无法摧毁敌人的城堡，所以返回 0 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= forts.length <= 1000</code></li>
	<li><code>-1 <= forts[i] <= 1</code></li>
</ul>

## 2512.奖励最顶尖的 K 名学生

[打开力扣](https://leetcode.cn/problems/reward-top-k-students) [我的代码](2512.reward_top_k_students.py)

给你两个字符串数组<code>positive_feedback</code> 和<code>negative_feedback</code>，分别包含表示正面的和负面的词汇。<strong>不会</strong>有单词同时是正面的和负面的。

一开始，每位学生分数为<code>0</code>。每个正面的单词会给学生的分数 <strong>加</strong><code>3</code>分，每个负面的词会给学生的分数 <strong>减</strong><code>1</code>分。

给你<code>n</code>个学生的评语，用一个下标从 <strong>0</strong>开始的字符串数组<code>report</code>和一个下标从 <strong>0</strong>开始的整数数组<code>student_id</code>表示，其中<code>student_id[i]</code>表示这名学生的 ID ，这名学生的评语是<code>report[i]</code>。每名学生的 ID <strong>互不相同</strong>。

给你一个整数<code>k</code>，请你返回按照得分<strong>从高到低</strong>最顶尖的<em></em><code>k</code>名学生。如果有多名学生分数相同，ID 越小排名越前。



<strong>示例 1：</strong>

<pre><b>输入：</b>positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is studious","the student is smart"], student_id = [1,2], k = 2
<b>输出：</b>[1,2]
<b>解释：</b>
两名学生都有 1 个正面词汇，都得到 3 分，学生 1 的 ID 更小所以排名更前。
</pre>

<strong>示例 2：</strong>

<pre><b>输入：</b>positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is not studious","the student is smart"], student_id = [1,2], k = 2
<b>输出：</b>[2,1]
<b>解释：</b>
- ID 为 1 的学生有 1 个正面词汇和 1 个负面词汇，所以得分为 3-1=2 分。
- ID 为 2 的学生有 1 个正面词汇，得分为 3 分。
学生 2 分数更高，所以返回 [2,1] 。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= positive_feedback.length, negative_feedback.length <= 10<sup>4</sup></code></li>
	<li><code>1 <= positive_feedback[i].length, negative_feedback[j].length <= 100</code></li>
	<li><code>positive_feedback[i]</code> 和<code>negative_feedback[j]</code>都只包含小写英文字母。</li>
	<li><code>positive_feedback</code> 和<code>negative_feedback</code>中不会有相同单词。</li>
	<li><code>n == report.length == student_id.length</code></li>
	<li><code>1 <= n <= 10<sup>4</sup></code></li>
	<li><code>report[i]</code>只包含小写英文字母和空格<code>' '</code>。</li>
	<li><code>report[i]</code>中连续单词之间有单个空格隔开。</li>
	<li><code>1 <= report[i].length <= 100</code></li>
	<li><code>1 <= student_id[i] <= 10<sup>9</sup></code></li>
	<li><code>student_id[i]</code>的值 <strong>互不相同</strong>。</li>
	<li><code>1 <= k <= n</code></li>
</ul>

## 2513.最小化两个数组中的最大值

[打开力扣](https://leetcode.cn/problems/minimize-the-maximum-of-two-arrays) [我的代码](2513.minimize_the_maximum_of_two_arrays.py)

给你两个数组<code>arr1</code> 和<code>arr2</code>，它们一开始都是空的。你需要往它们中添加正整数，使它们满足以下条件：

<ul>
	<li><code>arr1</code>包含<code>uniqueCnt1</code>个<strong>互不相同</strong>的正整数，每个整数都<strong>不能 </strong>被<code>divisor1</code><strong>整除</strong>。</li>
	<li><code>arr2</code>包含<code>uniqueCnt2</code>个<strong>互不相同</strong>的正整数，每个整数都<strong>不能</strong>被<code>divisor2</code><strong>整除</strong>。</li>
	<li><code>arr1</code> 和<code>arr2</code>中的元素<strong>互不相同</strong>。</li>
</ul>

给你<code>divisor1</code>，<code>divisor2</code>，<code>uniqueCnt1</code>和<code>uniqueCnt2</code>，请你返回两个数组中<strong>最大元素</strong>的<strong>最小值</strong>。



<strong>示例 1：</strong>

<pre>
<b>输入：</b>divisor1 = 2, divisor2 = 7, uniqueCnt1 = 1, uniqueCnt2 = 3
<b>输出：</b>4
<b>解释：</b>
我们可以把前 4 个自然数划分到 arr1 和 arr2 中。
arr1 = [1] 和 arr2 = [2,3,4] 。
可以看出两个数组都满足条件。
最大值是 4 ，所以返回 4 。
</pre>

<strong>示例 2：</strong>

<pre>
<b>输入：</b>divisor1 = 3, divisor2 = 5, uniqueCnt1 = 2, uniqueCnt2 = 1
<b>输出：</b>3
<b>解释：</b>
arr1 = [1,2] 和 arr2 = [3] 满足所有条件。
最大值是 3 ，所以返回 3 。</pre>

<strong>示例 3：</strong>

<pre>
<b>输入：</b>divisor1 = 2, divisor2 = 4, uniqueCnt1 = 8, uniqueCnt2 = 2
<b>输出：</b>15
<b>解释：</b>
最终数组为 arr1 = [1,3,5,7,9,11,13,15] 和 arr2 = [2,6] 。
上述方案是满足所有条件的最优解。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>2 <= divisor1, divisor2 <= 10<sup>5</sup></code></li>
	<li><code>1 <= uniqueCnt1, uniqueCnt2 < 10<sup>9</sup></code></li>
	<li><code>2 <= uniqueCnt1 + uniqueCnt2 <= 10<sup>9</sup></code></li>
</ul>

## 2514.统计同位异构字符串数目

[打开力扣](https://leetcode.cn/problems/count-anagrams) [我的代码](2514.count_anagrams.py)

给你一个字符串<code>s</code>，它包含一个或者多个单词。单词之间用单个空格<code>' '</code>隔开。

如果字符串 <code>t</code>中第 <code>i</code>个单词是 <code>s</code>中第 <code>i</code>个单词的一个<strong>排列</strong>，那么我们称字符串<code>t</code>是字符串<code>s</code>的同位异构字符串。

<ul>
	<li>比方说，<code>"acb dfe"</code>是<code>"abc def"</code>的同位异构字符串，但是<code>"def cab"</code>和<code>"adc bef"</code>不是。</li>
</ul>

请你返回<em></em><code>s</code>的同位异构字符串的数目，由于答案可能很大，请你将它对<code>10<sup>9</sup> + 7</code><strong>取余</strong> 后返回。



<strong>示例 1：</strong>

<pre><b>输入：</b>s = "too hot"
<b>输出：</b>18
<b>解释：</b>输入字符串的一些同位异构字符串为 "too hot" ，"oot hot" ，"oto toh" ，"too toh" 以及 "too oht" 。
</pre>

<strong>示例 2：</strong>

<pre><b>输入：</b>s = "aa"
<b>输出：</b>1
<strong>解释：</strong>输入字符串只有一个同位异构字符串。</pre>



<strong>提示：</strong>

<ul>
	<li><code>1 <= s.length <= 10<sup>5</sup></code></li>
	<li><code>s</code> 只包含小写英文字母和空格<code>' '</code>。</li>
	<li>相邻单词之间由单个空格隔开。</li>
</ul>
