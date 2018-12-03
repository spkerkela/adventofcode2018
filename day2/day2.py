#!/usr/bin/env python3
import sys


def contains_n(s, n):
    contained = {}
    for c in s:
        if c in contained:
            contained[c] = contained[c] + 1
        else:
            contained[c] = 1
    for v in contained.values():
        if v == n:
            return True

    return False


def process_ids(ids):
    contains_2 = len([id for id in ids if contains_n(id, 2)])
    contains_3 = len([id for id in ids if contains_n(id, 3)])
    print(contains_2, contains_3)
    return contains_2 * contains_3


if __name__ == '__main__':
    with open(sys.argv[1], 'r', encoding='utf-8') as input_file:
        ids = input_file.readlines()
        print(process_ids(ids))
