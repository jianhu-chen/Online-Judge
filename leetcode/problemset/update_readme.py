#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""更新README.md"""
import os
import re
import sys
import json
import os.path as osp

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 update_readme.py <filter>")
        print("       filter optional: all, top, hot100")
        sys.exit(1)

    filter_type = sys.argv[1]
    assert filter_type in ("all", "top", "hot100")
    save_file = {
        "all": "README.md",
        "top": "README_TOP.md",
        "hot100": "README_HOT100.md"
    }[filter_type]

    readme_title = {
        "all": "Leetcode",
        "top": "👨‍💻 LeetCode 精选 TOP 面试题",
        "hot100": "🔥 LeetCode 热题 HOT 100"
    }[filter_type]

    readme_head = {
        "all": "https://leetcode.cn/problemset/all/",
        "top": "https://leetcode.cn/problem-list/2cktkvj/",
        "hot100": "https://leetcode.cn/problem-list/2ckc81c/"
    }[filter_type]

    files = filter(
        lambda x: re.search(r"^\d+\.", x) and re.search(r"\.py$", x),
        os.listdir()
    )
    pids = map(lambda x: x.split(".")[0], files)
    # load problems
    with open(f"problems_{filter_type}.json", "r") as fp:
        problems = json.load(fp)
    problems = sorted(
        (problems[pid] for pid in pids if pid in problems),
        key=lambda x: int(x["frontendQuestionId"])
    )

    readme = """# {}

{}

| # | 英文标题 | 中文标题 | 我的代码 | 题目内容 | 难度 | 通过率 |
|:-:|---------|--------|---------|---------|-----|-------|
""".format(readme_title, readme_head)

    for q in problems:
        frontendQuestionId = q["frontendQuestionId"]
        titleSlug = q["titleSlug"]
        title = q["title"]
        titleCn = q["titleCn"]
        difficulty = q["difficulty"]
        acRate = q["acRate"]
        url = f"https://leetcode.cn/problems/{titleSlug}"
        file = f"{frontendQuestionId}.{titleSlug.replace('-', '_')}.py"
        file_md = file.replace(".py", ".md")
        readme += (f"|{frontendQuestionId}|[{title}]({url})|[{titleCn}]({url})|"
                   f"[{osp.basename(file)}]({file})|[点击打开]({file_md})|{difficulty}|{acRate:.2%}|\n")

    with open(save_file, "w") as fp:
        fp.write(readme)

    print("🎉 done")
