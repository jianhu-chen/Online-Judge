# 剑指 Offer 32 - II. 从上到下打印二叉树 II

[打开力扣](https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof) [我的代码](剑指 Offer 32 - II.cong_shang_dao_xia_da_yin_er_cha_shu_ii_lcof.py)

从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。



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
  [9,20],
  [15,7]
]
</pre>



<strong>提示：</strong>

<ol>
	<li><code>节点总数 <= 1000</code></li>
</ol>

注意：本题与主站 102 题相同：<a href="https://leetcode-cn.com/problems/binary-tree-level-order-traversal/">https://leetcode-cn.com/problems/binary-tree-level-order-traversal/</a>
