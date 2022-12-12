#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从力扣下载题目到本地."""
import re
import sys
import json
import os.path as osp

import requests

TEMPLET = """#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# {url}
{imp}
{code}
"""


def get_problem_by_slug(slug: str) -> dict:
    url = "https://leetcode.cn/graphql"
    params = {
        "operationName": "getQuestionDetail",
        "variables": {"titleSlug": slug},
        "query": """query getQuestionDetail($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                questionFrontendId
                questionTitle
                questionTitleSlug
                content
                difficulty
                stats
                similarQuestions
                categoryTitle
                topicTags {
                        name
                        slug
                }
                translatedContent
                translatedTitle
                codeSnippets {
                    lang
                    code
                }
            }
        }"""
    }

    json_data = json.dumps(params).encode('utf8')
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        ),
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Referer": "https://leetcode.cn/problems/" + slug
    }
    resp = requests.post(url, data=json_data, headers=headers, timeout=10)
    content = resp.json()

    # 题目详细信息
    question = content['data']['question']
    return question


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 pull_problem.py <id>")
        sys.exit(1)

    id = sys.argv[1]
    # load problems
    with open("problems_all.json", "r") as fp:
        problems = json.load(fp)

    if id not in problems:
        print(f"Problem {id} not found, try to update problems.json first.")
        sys.exit(1)

    q = problems[id]
    print("problem info:\n", json.dumps(q, indent=2, ensure_ascii=False))

    if q["paidOnly"]:
        print("This problem is 'paidOnly'!")
        sys.exit(1)

    frontendQuestionId = q["frontendQuestionId"]
    titleSlug = q["titleSlug"]

    file = f"{frontendQuestionId}.{titleSlug.replace('-', '_')}.py"
    file_md = file.replace(".py", ".md")
    question = get_problem_by_slug(titleSlug)
    codeSnippets = question["codeSnippets"]
    try:
        code = list(filter(lambda x: x["lang"] == "Python3", codeSnippets))[0]["code"]
    except Exception:
        code = ""
    questionTitle = question["questionTitle"]
    translatedTitle = question["translatedTitle"]
    translatedContent = question["translatedContent"]
    url = f"https://leetcode.cn/problems/{titleSlug}"

    with open(file, "w") as fp:
        fp.write(
            TEMPLET.format(
                url=url,
                imp="from typing import List\n\n" if "List" in code else "",
                code=code
            )
        )

    # README
    content = re.sub(r"<p>|</p>|&nbsp;", "", translatedContent).strip()
    content = content.replace("&lt;", "<")
    content = content.replace("&gt;", ">")

    with open(file_md, "w") as fp:
        fp.write("# {}. {}\n\n".format(frontendQuestionId, translatedTitle))
        fp.write("[打开力扣]({}) [我的代码]({})\n\n".format(url, osp.basename(file)))
        fp.write(content)

    print("🎉 save to {}".format(file))
