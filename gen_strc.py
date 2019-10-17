# -*- encoding: utf-8 -*-
'''
@File    :   gen_strc.py
@Time    :   2019/10/17 11:45:41
@Author  :   jhchen
@E-mail  :   jianhuchen@163.com
@License :   Copyright, USTC
@Desc    :   For generate table of Markdown format.
'''

# here put the import lib
import os

def main():
    path = './Offer-Python'

    files = [f for f in os.listdir(path) if f.endswith('.py')]
    files = sorted(files, key=lambda f: eval(f.split('.')[0]))
    py_path = [os.path.join('Offer-Python', f) for f in files]
    cpp_path = [os.path.join('Offer-Cpp', f.replace('.py', '.cpp')) for f in files]
    
    lines = []
    for f, p, c in zip(files, py_path, cpp_path):
        name = f.replace('.py', '')
        line = '|'.join(
            ['', 
            name, 
            '[{}]({})'.format(name, p), 
            '[{}]({})'.format(name, c), 
            '']
            )
        lines.append(line)
    
    for l in lines:
        print(l)



if __name__ == "__main__":
    main()