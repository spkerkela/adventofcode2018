#!/usr/bin/env python3
import sys
import itertools


def parse(line):
    try:
        return int(line)
    except Exception as e:
        print(e)
        return 0


def repeats(changeset):
    cycling_set = itertools.cycle(changeset)
    current_frequency = 0
    frequencies_seen = {current_frequency}

    for change in cycling_set:
        current_frequency = current_frequency + change
        if current_frequency in frequencies_seen:
            return current_frequency
        else:
            frequencies_seen.add(current_frequency)


def calculate_frequency(changeset):
    return sum(changeset)


if __name__ == '__main__':
    with open(sys.argv[1], 'r', encoding='utf-8') as input_file:
        changeset = [parse(line) for line in input_file.readlines()]
        print(calculate_frequency(changeset))
        print(repeats(changeset))
