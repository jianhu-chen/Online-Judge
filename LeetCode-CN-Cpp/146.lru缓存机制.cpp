/*
 * @lc app=leetcode.cn id=146 lang=cpp
 *
 * [146] LRU缓存机制
 *
 * https://leetcode-cn.com/problems/lru-cache/description/
 *
 * algorithms
 * Medium (50.45%)
 * Likes:    822
 * Dislikes: 0
 * Total Accepted:    91.5K
 * Total Submissions: 181.2K
 * Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
 *
 * 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
 * 
 * 获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
 * 写入数据 put(key, value) -
 * 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
 * 
 * 
 * 
 * 进阶:
 * 
 * 你是否可以在 O(1) 时间复杂度内完成这两种操作？
 * 
 * 
 * 
 * 示例:
 * 
 * LRUCache cache = new LRUCache( 2 / 缓存容量 / );
 * 
 * cache.put(1, 1);
 * cache.put(2, 2);
 * cache.get(1);       // 返回  1
 * cache.put(3, 3);    // 该操作会使得关键字 2 作废
 * cache.get(2);       // 返回 -1 (未找到)
 * cache.put(4, 4);    // 该操作会使得关键字 1 作废
 * cache.get(1);       // 返回 -1 (未找到)
 * cache.get(3);       // 返回  3
 * cache.get(4);       // 返回  4
 * 
 * 
 */

// @lc code=start
#include <iostream>
#include <map>

using namespace std;

class Node
{
public:
    int key, val;
    Node *prev, *next;
    Node(int key, int val)
    {
        this->key = key;
        this->val = val;
    }
};

class DoubleList
{
public:
    DoubleList()
    {
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head->next = tail;
        tail->prev = head;
        size = 0;
    }

    // 在链表末尾增加新的节点
    void addLast(Node *x)
    {
        x->prev = tail->prev;
        x->next = tail;
        tail->prev->next = x;
        tail->prev = x;
        size++;
    }

    // 删除链表中的节点: x
    void remove(Node *x)
    {
        x->prev->next = x->next;
        x->next->prev = x->prev;
        size--;
    }

    Node *removeFirst()
    {
        if (head->next == tail)
        {
            return nullptr;
        }

        Node *first = head->next;
        remove(head->next);
        return first;
    }

    int getSize()
    {
        return size;
    }

private:
    Node *head, *tail;
    int size;
};

class LRUCache
{
public:
    LRUCache(int capacity)
    {
        cap = capacity;
    }

    int get(int key)
    {
        auto x = hashMap.find(key);
        if (x == hashMap.end())
        {
            return -1;
        }
        else{
            makeRecently(key);
            return x->second->val;
        }

    }

    void put(int key, int value)
    {
        auto x = hashMap.find(key);
        // 存在
        if (x != hashMap.end())
        {
            deleteKey(key);
        }
        
        // 若容量已满
        if (cache.getSize() == cap)
        {
            deleteLeastRecently();
        }

        addRecently(key, value);
    }

private:
    map<int, Node *> hashMap;
    DoubleList cache;
    int cap;

    // 将某个key提升为最近使用
    void makeRecently(int key)
    {
        auto x = hashMap.find(key);
        // 先从链表中删除这个节点
        cache.remove(x->second);
        // 重新插到队尾
        cache.addLast(x->second);
    }

    // 添加最新使用的元素
    void addRecently(int key, int val)
    {
        Node *x = new Node(key, val);
        cache.addLast(x);
        hashMap[key] = x;
    }

    // 删除某一个key
    void deleteKey(int key)
    {
        auto x = hashMap.find(key);
        cache.remove(x->second);
        hashMap.erase(key);
    }

    // 删除最久未使用的元素
    void deleteLeastRecently()
    {
        Node *deleteNode = cache.removeFirst();
        hashMap.erase(deleteNode->key);
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
// @lc code=end
