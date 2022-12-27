#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Employee:
    def __init__(self, happy, subordinates=[]) -> None:
        self.happy = happy
        self.subordinates = subordinates


class MaximumHappiness:
    """https://www.nowcoder.com/practice/a5f542742fe24181b28f7d5b82e2e49a."""

    def solution(self, emp: Employee):
        def process(e: Employee, go: bool):
            if go:
                result = e.happy
                for sub in e.subordinates:
                    result += process(sub, False)
            else:
                result = 0
                for sub in e.subordinates:
                    result += max(process(sub, True), process(sub, False))
            return result
        return max(process(emp, True), process(emp, False))


if __name__ == "__main__":
    n = 3
    root = 1
    b = Employee(1)
    c = Employee(1)
    a = Employee(5, subordinates=[b, c])
    print(MaximumHappiness().solution(a))
