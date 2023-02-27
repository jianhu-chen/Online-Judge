# 剑指 Offer 68 - I. 二叉搜索树的最近公共祖先

[打开力扣](https://leetcode.cn/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof) [我的代码](剑指 Offer 68 - I.er_cha_sou_suo_shu_de_zui_jin_gong_gong_zu_xian_lcof.py)

给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

<a href="https://baike.baidu.com/item/%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88/8918834?fr=aladdin" target="_blank">百度百科</a>中最近公共祖先的定义为：&ldquo;对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（<strong>一个节点也可以是它自己的祖先</strong>）。&rdquo;

例如，给定如下二叉搜索树: root =[6,2,8,0,4,7,9,null,null,3,5]

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/binarysearchtree_improved.png">



<strong>示例 1:</strong>

<pre><strong>输入:</strong> root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
<strong>输出:</strong> 6
<strong>解释: </strong>节点 <code>2 </code>和节点 <code>8 </code>的最近公共祖先是 <code>6。</code>
</pre>

<strong>示例 2:</strong>

<pre><strong>输入:</strong> root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
<strong>输出:</strong> 2
<strong>解释: </strong>节点 <code>2</code> 和节点 <code>4</code> 的最近公共祖先是 <code>2</code>, 因为根据定义最近公共祖先节点可以为节点本身。</pre>



<strong>说明:</strong>

<ul>
	<li>所有节点的值都是唯一的。</li>
	<li>p、q 为不同节点且均存在于给定的二叉搜索树中。</li>
</ul>

注意：本题与主站 235 题相同：<a href="https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/">https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/</a>
