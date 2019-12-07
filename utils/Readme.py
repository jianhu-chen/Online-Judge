# -*- encoding: utf-8 -*-
'''
@File    :   Readme.py
@Time    :   2019/11/15 15:22:41
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   A script that generates the README document.
'''

# here put the import lib
import os
import re
import requests

from lxml import etree


readme_content = '''# Online-Judge

# 目录说明

- utils：小工具包

> 部分链接显示page not found, 因为还没写完。

# 剑指Offer

offer_placeholder

# LeetCode

leetcode_placeholder

# PAT(BasicLevel)

pat_basic_placeholder

'''


class Readme:
    def __init__(self, offer_path, leetcode_path, pat_basic_path):
        self.offer_path = offer_path
        self.leetcode_path = leetcode_path
        self.pat_basic_path = pat_basic_path
        self.tabel_head = '''| ID   | Title | Python | C++  |
| :----: | :-----: | :------: | :----: |
'''

    def generate(self, out_path):
        offer_tabel = self.generate_offer_tabel(self.offer_path)
        content = readme_content.replace('offer_placeholder', offer_tabel)

        pat_basic_tabel = self.generate_pat_basic_tabel(self.pat_basic_path)
        content = content.replace('pat_basic_placeholder', pat_basic_tabel)

        leetcode_tabel = self.generate_leetcode_tabel(self.leetcode_path)
        content = content.replace('leetcode_placeholder', leetcode_tabel)

        with open(os.path.join(out_path, 'README.md'), 'w') as fp:
            fp.write(content)
        print('Compelte!')

    def generate_leetcode_tabel(self, leetcode_path):
        lines = []
        path = leetcode_path[0]
        files = [f for f in os.listdir(path) if f[0].isdigit()]
        files.sort(key=lambda x: int(x.split('.')[0]))
        for file_name in files:
            problem_id = file_name.split('.')[0]
            problem_name = file_name[file_name.index(
                '.')+1:].replace('.py', '').replace('.cpp', '')
            py_file_path = os.path.join(leetcode_path[0].split(
                '/')[-1], '{}.{}.py'.format(problem_id, problem_name))
            cpp_file_path = os.path.join(leetcode_path[1].split(
                '/')[-1],  '{}.{}.cpp'.format(problem_id, problem_name))
            line = '|'.join(
                ['', problem_id, '[{}](https://leetcode.com/problems/{})'.format(problem_name, problem_name), 'NonePy', 'NoneCpp', ''])
            if os.path.exists(py_file_path):
                line = line.replace('NonePy', '[{}]({})'.format(
                    'Python', py_file_path))
            if os.path.exists(cpp_file_path):
                line = line.replace('NoneCpp', '[{}]({})'.format(
                    'C++', cpp_file_path))
            lines.append(line)
        tabel = self.tabel_head + '\n'.join(lines)
        return tabel

    def generate_pat_basic_tabel(self, pat_basic_path):
        lines = []
        path = pat_basic_path[1]
        files = [f for f in os.listdir(path) if f[0].isdigit()]
        files.sort(key=lambda x: int(x.split('.')[0]))
        for file_name in files:
            problem_id = file_name.split('.')[0]
            problem_name = file_name[file_name.index(
                '.')+1:].replace('.py', '').replace('.cpp', '')
            py_file_path = os.path.join(pat_basic_path[0].split(
                '/')[-1], '{}.{}.py'.format(problem_id, problem_name))
            cpp_file_path = os.path.join(pat_basic_path[1].split(
                '/')[-1],  '{}.{}.cpp'.format(problem_id, problem_name))
            with open(cpp_file_path, 'r') as fp:
                content = fp.read()
                link = '|'.join(re.findall(r'// 题目链接: (.*)', content))
            line = '|'.join(
                ['', problem_id, '[{}]({})'.format(problem_name, link), 'NonePy', 'NoneCpp', ''])
            if os.path.exists(py_file_path):
                line = line.replace('NonePy', '[{}]({})'.format(
                    'Python', py_file_path))
            if os.path.exists(cpp_file_path):
                line = line.replace('NoneCpp', '[{}]({})'.format(
                    'C++', cpp_file_path))
            lines.append(line)
        tabel = self.tabel_head + '\n'.join(lines)
        return tabel

    def generate_offer_tabel(self, offer_path):
        links = []
        for i in range(1, 5):
            response = requests.get(
                'https://www.nowcoder.com/ta/coding-interviews?query=&asc=true&order=&tagQuery=&page={}'.format(i))
            html = etree.HTML(response.text)
            one_page_links = html.xpath('//table/tbody/tr/td/a/@href')
            links.extend(one_page_links)
        lines = []
        path = offer_path[0]
        files = [f for f in os.listdir(path) if f[0].isdigit()]
        files.sort(key=lambda x: int(x.split('.')[0]))
        for file_name in files:
            problem_id = file_name.split('.')[0]
            problem_name = file_name[file_name.index(
                '.')+1:].replace('.py', '').replace('.cpp', '')
            py_file_path = os.path.join(offer_path[0].split(
                '/')[-1], '{}.{}.py'.format(problem_id, problem_name))
            cpp_file_path = os.path.join(offer_path[1].split(
                '/')[-1],  '{}.{}.cpp'.format(problem_id, problem_name))
            line = '|'.join(
                ['', problem_id, '[{}](https://www.nowcoder.com/{})'.format(problem_name, links[eval(problem_id)-1]), 'NonePy', 'NoneCpp', ''])
            if os.path.exists(py_file_path):
                line = line.replace('NonePy', '[{}]({})'.format(
                    'Python', py_file_path))
            if os.path.exists(cpp_file_path):
                line = line.replace('NoneCpp', '[{}]({})'.format(
                    'C++', cpp_file_path))

            lines.append(line)
        tabel = self.tabel_head + '\n'.join(lines)
        return tabel


if __name__ == "__main__":
    offer_path = ['./Offer-Python', './Offer-Cpp']
    leetcode_path = ['./LeetCode-Python', './LeetCode-Cpp']
    pat_path = ['./PAT(BasicLevel)-Python', './PAT(BasicLevel)-Cpp']
    readme = Readme(offer_path, leetcode_path, pat_path)
    readme.generate('./')
