#!/usr/bin/env python3
import sys
import difflib


def find_pair(ids):
    for left in ids:
        for right in ids:
            if left == right:
                continue
            else:
                l, r = left.rstrip(), right.rstrip()
                diffs = [(n, f) for (n, f) in enumerate(difflib.ndiff(
                    l, r)) if f.startswith('-')]
                if len(diffs) == 1:
                    return (l, r, diffs[0][0])
    return None


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
        (left, right, index) = find_pair(ids)
        newstr = left[:index] + left[index+1:]
        print(newstr)
