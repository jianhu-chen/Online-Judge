# 剑指 Offer 35. 复杂链表的复制

[打开力扣](https://leetcode.cn/problems/fu-za-lian-biao-de-fu-zhi-lcof) [我的代码](剑指 Offer 35.fu_za_lian_biao_de_fu_zhi_lcof.py)

请实现 <code>copyRandomList</code> 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 <code>next</code> 指针指向下一个节点，还有一个 <code>random</code> 指针指向链表中的任意节点或者 <code>null</code>。



<strong>示例 1：</strong>

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e1.png">

<pre><strong>输入：</strong>head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
<strong>输出：</strong>[[7,null],[13,0],[11,4],[10,2],[1,0]]
</pre>

<strong>示例 2：</strong>

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e2.png">

<pre><strong>输入：</strong>head = [[1,1],[2,1]]
<strong>输出：</strong>[[1,1],[2,1]]
</pre>

<strong>示例 3：</strong>

<strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e3.png"></strong>

<pre><strong>输入：</strong>head = [[3,null],[3,0],[3,null]]
<strong>输出：</strong>[[3,null],[3,0],[3,null]]
</pre>

<strong>示例 4：</strong>

<pre><strong>输入：</strong>head = []
<strong>输出：</strong>[]
<strong>解释：</strong>给定的链表为空（空指针），因此返回 null。
</pre>



<strong>提示：</strong>

<ul>
	<li><code>-10000 <= Node.val <= 10000</code></li>
	<li><code>Node.random</code>为空（null）或指向链表中的节点。</li>
	<li>节点数目不超过 1000 。</li>
</ul>



<strong>注意：</strong>本题与主站 138 题相同：<a href="https://leetcode-cn.com/problems/copy-list-with-random-pointer/">https://leetcode-cn.com/problems/copy-list-with-random-pointer/</a>
