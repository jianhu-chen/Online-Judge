# 剑指 Offer 32 - III. 从上到下打印二叉树 III

[打开力扣](https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof) [我的代码](剑指 Offer 32 - III.cong_shang_dao_xia_da_yin_er_cha_shu_iii_lcof.py)

请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。



例如:<br>
给定二叉树:<code>[3,9,20,null,null,15,7]</code>,

<pre>    3
   / \
  9  20
    /  \
   15   7
</pre>

返回其层次遍历结果：

<pre>[
  [3],
  [20,9],
  [15,7]
]
</pre>



<strong>提示：</strong>

<ol>
	<li><code>节点总数 <= 1000</code></li>
</ol>
