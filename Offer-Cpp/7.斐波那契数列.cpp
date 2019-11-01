//
// Created by jhchen on 2019/11/1.
//

//    题目描述
//    大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
//    n<=39

#include <iostream>

using namespace std;

// 动态规划 时间复杂度O(n)
class Solution {
public:
    int Fibonacci(int n) {

    }
};


// 循环法
//运行时间：4ms
//占用内存：584k
/*class Solution {
public:
    int Fibonacci(int n) {
        if (n == 0) {
            return 0;
        }
        if (n == 1 || n == 2) {
            return 1;
        }
        int fir = 1;
        int sec = 1;
        int ret;
        for (int i = 3; i <= n; ++i) {
            ret = fir + sec;
            fir = sec;
            sec = ret;
        }
        return ret;
    }
};*/


// 递归法
//运行时间：755ms
//占用内存：488k
/*class Solution {
public:
    int Fibonacci(int n) {
        if(n==0){
            return 0;
        }
        if (n==1 || n==2){
            return 1;
        }
        return Fibonacci(n-1) + Fibonacci(n-2);
    }
};*/

