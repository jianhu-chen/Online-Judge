//
// Created by jhchen<jianhuchen@163.com> on 2019-11-12 15:03:29.
//
// 题目链接: https://pintia.cn/problem-sets/994805260223102976/problems/994805321640296448
// 题目描述: 读入 $$n$$（$$>0$$）名学生的姓名、学号、成绩，分别输出成绩最高和成绩最低学生的姓名和学号。
// 
// ### 输入格式：
// 
// 每个测试输入包含 1 个测试用例，格式为
// ```
// 第 1 行：正整数 n
// 第 2 行：第 1 个学生的姓名 学号 成绩
// 第 3 行：第 2 个学生的姓名 学号 成绩
//   ... ... ...
// 第 n+1 行：第 n 个学生的姓名 学号 成绩
// ```
// 其中`姓名`和`学号`均为不超过 10 个字符的字符串，成绩为 0 到 100 之间的一个整数，这里保证在一组测试用例中没有两个学生的成绩是相同的。
// 
// ### 输出格式：
// 
// 对每个测试用例输出 2 行，第 1 行是成绩最高学生的姓名和学号，第 2 行是成绩最低学生的姓名和学号，字符串间有 1 空格。
// 
// ### 输入样例：
// ```in
// 3
// Joe Math990112 89
// Mike CS991301 100
// Mary EE990830 95
// ```
// 
// ### 输出样例：
// ```out
// Mike CS991301
// Joe Math990112
// ```

#include <iostream>
#include <string>

using namespace std;

int main() {
    int n, stu_score, max_score=-1, min_score=101;
    string stu_name, stu_num;
    string max_stu_name, max_stu_num, min_stu_name, min_stu_num;;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> stu_name >> stu_num >> stu_score;
        if(stu_score>max_score){
            max_score = stu_score;
            max_stu_name =stu_name;
            max_stu_num =stu_num;
        }
        if(stu_score<min_score){
            min_score = stu_score;
            min_stu_name = stu_name;
            min_stu_num = stu_num;
        }
    }
    cout << max_stu_name << " " << max_stu_num<<endl;
    cout << min_stu_name << " " << min_stu_num<<endl;
    return 0;
}
            