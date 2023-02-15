# 剑指 Offer 04. 二维数组中的查找

[打开力扣](https://leetcode.cn/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof) [我的代码](剑指 Offer 04.er_wei_shu_zu_zhong_de_cha_zhao_lcof.py)

在一个 n * m 的二维数组中，每一行都按照从左到右<strong>非递减</strong>的顺序排序，每一列都按照从上到下<strong>非递减</strong>的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。



<strong>示例:</strong>

现有矩阵 matrix 如下：

<pre>
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
</pre>

给定 target=<code>5</code>，返回<code>true</code>。

给定target=<code>20</code>，返回<code>false</code>。



<strong>限制：</strong>

<code>0 <= n <= 1000</code>

<code>0 <= m <= 1000</code>



<strong>注意：</strong>本题与主站 240 题相同：<a href="https://leetcode-cn.com/problems/search-a-2d-matrix-ii/">https://leetcode-cn.com/problems/search-a-2d-matrix-ii/</a>
