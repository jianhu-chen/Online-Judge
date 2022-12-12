#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从力扣下载题库到本地."""
import sys
import json

import requests


def query_all_problems(filters={}):
    questions = []
    url = "https://leetcode.cn/graphql"
    skip = 0
    limit = 100
    hasMore = True
    while hasMore:
        print("get problems from {} to {}".format(skip, skip + limit))
        params = {
            "variables": {"categorySlug": "", "skip": skip, "limit": limit, "filters": filters},
            "query": """query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
                problemsetQuestionList(
                    categorySlug: $categorySlug
                    limit: $limit
                    skip: $skip
                    filters: $filters
                ) {
                    hasMore
                    total
                    questions {
                        acRate
                        difficulty
                        freqBar
                        frontendQuestionId
                        isFavor
                        paidOnly
                        solutionNum
                        status
                        title
                        titleCn
                        titleSlug
                        topicTags {
                            name
                            nameTranslated
                            id
                            slug
                        }
                        extra {
                            hasVideoSolution
                                topCompanyTags {
                                imgUrl
                                slug
                                numSubscribed
                            }
                        }
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
            "Referer": "https://leetcode.cn/problems/all"
        }
        resp = requests.post(url, data=json_data, headers=headers, timeout=10)
        resp_json = resp.json()
        hasMore = resp_json['data']['problemsetQuestionList']['hasMore']
        qs = resp_json['data']['problemsetQuestionList']['questions']
        if hasMore:
            assert len(qs) == limit
        questions.extend(qs)
        skip += limit
    return questions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 pull_problems.py <filter>")
        print("       filter optional: all, top, hot100")
        sys.exit(1)

    if sys.argv[1] == "all":
        filters = {}
    elif sys.argv[1] == "hot100":
        filters = {"listId": "2cktkvj"}
    elif sys.argv[1] == "top":
        filters = {"listId": "2ckc81c"}
    else:
        print("unknow paramters {}, only supports 'all', 'hot100' and 'top'".format(sys.argv[1]))
        sys.exit(1)

    problems = query_all_problems(filters)
    save_keys = [
        "acRate",
        "difficulty",
        "paidOnly",
        "frontendQuestionId",
        "title",
        "titleCn",
        "titleSlug",
    ]
    problems = {
        p["frontendQuestionId"]: {k: v for k, v in p.items() if k in save_keys}
        for p in problems
    }
    save_file = f"problems_{sys.argv[1]}.json"
    with open(save_file, "w") as fp:
        json.dump(problems, fp, indent=2, ensure_ascii=False)
    print(f"🎉 save to {save_file}")
