# -*- encoding: utf-8 -*-
'''
@File    :   Readme.py
@Time    :   2019/11/15 15:22:41
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright(C), USTC
@Desc    :   A script that generates a README document.
'''

# here put the import lib
import os

from Spider import *

readme_content = '''# Online-Judge

## 目录说明

- utils：小工具包

## 剑指Offer

offer_placeholder

## LeetCode

leetcode_placeholder

## PAT(BasicLevel)

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

        with open(os.path.join(out_path, 'README.md'), 'w') as fp:
            fp.write(content)
        print('Compelte!')

    def generate_pat_basic_tabel(self, pat_basic_path):
        lines = []
        path = pat_basic_path[1]
        files = [f for f in os.listdir(path) if f[0].isdigit()]
        files.sort(key=lambda x: int(x.split('.')[0]))
        for file_name in files:
            problem_id = file_name.split('.')[0]
            problem_name = file_name[file_name.index(
                '.')+1:].replace('.py', '').replace('.cpp', '')
            # py_file_path = os.path.join(pat_basic_path[0].split(
            #     '/')[-1], '{}.{}.py'.format(problem_id, problem_name))
            cpp_file_path = os.path.join(pat_basic_path[1].split(
                '/')[-1],  '{}.{}.cpp'.format(problem_id, problem_name))
            # line = '|'.join(['', problem_id, problem_name, '[{}]({})'.format(
            #     'Python', py_file_path), '[{}]({})'.format('C++', cpp_file_path), ''])
            line = '|'.join(['', problem_id, problem_name, 'None',
                             '[{}]({})'.format('C++', cpp_file_path), ''])
            lines.append(line)
        tabel = self.tabel_head + '\n'.join(lines)
        return tabel

    def generate_offer_tabel(self, offer_path):
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
            line = '|'.join(['', problem_id, problem_name, '[{}]({})'.format(
                'Python', py_file_path), '[{}]({})'.format('C++', cpp_file_path), ''])
            lines.append(line)
        tabel = self.tabel_head + '\n'.join(lines)
        return tabel


if __name__ == "__main__":
    offer_path = ['../Offer-Python', '../Offer-Cpp']
    leetcode_path = ['../LeetCode-Python']
    pat_path = ['../PAT(BasicLevel)-Cpp', '../PAT(BasicLevel)-Cpp']
    readme = Readme(offer_path, leetcode_path, pat_path)
    readme.generate('../')
