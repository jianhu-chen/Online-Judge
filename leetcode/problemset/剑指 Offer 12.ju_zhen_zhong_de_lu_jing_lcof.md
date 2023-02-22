# 剑指 Offer 12. 矩阵中的路径

[打开力扣](https://leetcode.cn/problems/ju-zhen-zhong-de-lu-jing-lcof) [我的代码](剑指 Offer 12.ju_zhen_zhong_de_lu_jing_lcof.py)

给定一个<code>m x n</code> 二维字符网格<code>board</code> 和一个字符串单词<code>word</code> 。如果<code>word</code> 存在于网格中，返回 <code>true</code> ；否则，返回 <code>false</code> 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。



例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word2.jpg" style="width: 322px; height: 242px;" />



<strong>示例 1：</strong>

<pre>
<strong>输入：</strong>board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
<strong>输出：</strong>true
</pre>

<strong>示例 2：</strong>

<pre>
<strong>输入：</strong>board = [["a","b"],["c","d"]], word = "abcd"
<strong>输出：</strong>false
</pre>



<strong>提示：</strong>

<ul>
	<li><code>m == board.length</code></li>
	<li><code>n = board[i].length</code></li>
	<li><code>1 <= m, n <= 6</code></li>
	<li><code>1 <= word.length <= 15</code></li>
	<li><code>board </code>和<code> word </code>仅由大小写英文字母组成</li>
</ul>

<strong>注意：</strong>本题与主站 79 题相同：<a href="https://leetcode-cn.com/problems/word-search/">https://leetcode-cn.com/problems/word-search/</a>
