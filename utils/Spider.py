# -*- encoding: utf-8 -*-
'''
@File    :   Spider.py
@Time    :   2019/11/12 10:04:28
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   A spider that gets the problem id, problem name,
            and problem content of the PAT page and generates
            the initial cpp file and cmakelists file.
'''

# here put the import lib
import os
import time
import json
import requests


class Spider:

    def __init__(self, cookies):
        '''
        cookie: must a dict, your cookie after login
        '''
        self.headers = {
            'Accept': r'application/json;charset=UTF-8',
            "User-Agent": r"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
        }
        self.cookies = cookies
        self.sess = requests.session()

    def run(self):
        print('get your info...')
        user_info = self.get_user_info()
        nickname = user_info.get('user').get('nickname')
        email = user_info.get('user').get('email')
        print('='*40)
        print('nickname: {}\temail: {}'.format(nickname, email))
        print('='*40)

        print('get problem sets info...')
        problem_sets = self.get_problem_sets().get('problemSets')
        print('='*40)
        print('id\tproblem_set_name')
        print('-'*40)
        for item in problem_sets:
            print('{}\t{}'.format(item.get('id'), item.get('name')))
        print('='*40)

        is_gen_cpp = input(
            'generate initial cpp file and cmakelists file(CMakeLists.txt)?y/[n]')
        if is_gen_cpp == 'y':
            problem_set_id = input('input problem set id:[994805260223102976]')
            if problem_set_id == '':
                problem_set_id = '994805260223102976'
            
            exam_id = 0
            for item in problem_sets:
                if item.get('id') == problem_set_id:
                    exam_id = item.get('exam').get('id')

            output_path = input('input initial cpp file output path:[./]')
            if output_path == '':
                output_path = './'
            try:
                self.generate_init_cpp(problem_set_id, exam_id, output_path)
                self.gen_cmakelists(output_path.split('/')[-1], output_path)
            except Exception as e:
                print(
                    'Error: please checkout problem_set_id or output_path of your input?')
                print(e)
            else:
                print('Complete!')

    def gen_cmakelists(self, project_name, file_path):
        file_list = [f for f in os.listdir(file_path) if f.endswith('.cpp')]
        file_list.sort(key=lambda f: int(f.split('.')[0]))
        file_head = '''cmake_minimum_required(VERSION 3.14)
project({})

set(CMAKE_CXX_STANDARD 11)\n
'''.format(project_name)
        line_list = []
        for f in file_list:
            f = f.replace('(', '\(').replace(')', '\)')
            line_list.append(
                'add_executable({} {})'.format(f.split('.')[0], f))

        file_content = file_head + '\n'.join(line_list)
        with open(os.path.join(file_path, 'CMakeLists.txt'), 'w') as fp:
            fp.write(file_content)

    def get_problem_info(self, problem_set_id, problem_id):
        problem_url = 'https://pintia.cn/api/problem-sets/{}/problems/{}'.format(
            problem_set_id, problem_id)
        suss_flag = False
        while suss_flag == False:
            try:
                response = self.sess.get(url=problem_url,
                                         headers=self.headers, cookies=self.cookies)
                problem_info = response.json().get('problemSetProblem')
                problem_label = problem_info.get('label')
                problem_title = problem_info.get('title')
                problem_content = problem_info.get('content')
                cpp_file_name = '{}.{}.cpp'.format(
                    problem_label, problem_title)
            except:
                pass
            else:
                suss_flag = True
        return cpp_file_name, problem_content

    def generate_init_cpp(self, problem_set_id, exam_id, output_path):
        problem_set_url = r'https://pintia.cn/api/problem-sets/{}/problem-list?exam_id={}&problem_type=PROGRAMMING&page=0&limit=200'.format(
            problem_set_id, exam_id)
        response = self.sess.get(url=problem_set_url,
                                 headers=self.headers, cookies=self.cookies)
        problem_list = response.json().get('problemSetProblems')
        for i, problem in enumerate(problem_list):
            problem_id = problem.get('id')
            problem_url = 'https://pintia.cn/problem-sets/{}/problems/{}'.format(
                problem_set_id, problem_id)
            cpp_file_name, problem_content = self.get_problem_info(
                problem_set_id, problem_id)
            file_head = '''//
// Created by jhchen<jianhuchen@163.com> on {}.
//
// 题目链接: {}
// 题目描述: '''.format(time.strftime('%Y-%m-%d %H:%M:%S'), problem_url)
            problem_content = problem_content.replace('\n', '\n// ')
            file_main = '''
#include <iostream>

using namespace std;

int main(){


    return 0;
}
            '''
            file_content = file_head + problem_content[:-3] + file_main
            with open(os.path.join(output_path, cpp_file_name), 'w') as fp:
                fp.write(file_content)
            print('[{}/{}] generate file : {}'.format(i+1, len(problem_list), os.path.join(
                output_path, cpp_file_name)))

    def get_user_info(self):
        url = 'https://pintia.cn/api/u/current'
        response = self.sess.get(
            url=url, headers=self.headers, cookies=self.cookies)
        user_info = response.json()
        return user_info

    def get_problem_sets(self):
        url = 'https://pintia.cn/api/problem-sets/always-available'
        response = self.sess.get(
            url=url, headers=self.headers, cookies=self.cookies)
        problem_sets = response.json()
        return problem_sets


if __name__ == "__main__":
    # 填PTASession这一个字段就行了
    cookies = {
        # '_ga': 'xxxxxxxxxxxx',
        # '_9755xjdesxxd_': '32',
        # 'JSESSIONID': '944842C76113F4AA8859BB904C6156F0',
        # '_gid': 'GA1.2.476729300.1573523772',
        # 'gdxidpyhxdE': r'XDymlTMTJoTT0S%2B5zwM8BEj5va0SZOBauYRVGw1H3W%2FlrPLZAJQ6dXzNDi7Qbs6aMu87GjyN8CjTqAXNMciSCRT515sRtn8HuR4t%2Frbxw319S4bOpZMhsioH%2BUtXz3z%5C5O%2F1zlmoAZ%2FAbMOPtbq2ZNHUUXDTL4L%5CSoVo5M5yxnA7g8UV%3A1573525489058',
        'PTASession': 'b0541733-df3f-4d07-864d-7c402573400',
        # '_gat': '1'
    }
    spider = Spider(cookies=cookies)
    spider.run()
