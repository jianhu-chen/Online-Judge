#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re

lines = []
for x in os.listdir("."):
    res = re.search(r"^CF(\d+)([\w\d]+).py$", x)
    if not res:
        continue
    lines.append((
        (f"* [{res.group(0)[:-3]}](https://codeforces.com/"
         f"contest/{res.group(1)}/problem/{res.group(2)})"),
        res.group(1),
        res.group(2)
    ))

lines.sort(key=lambda x: (x[1], x[2]))
with open("README.md", "w") as fp:
    fp.write("""## Codeforces AC Codes

{}
""".format('\n'.join([x[0] for x in lines])))
print("done.")
