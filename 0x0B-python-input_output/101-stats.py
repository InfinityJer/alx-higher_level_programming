#!/usr/bin/python3

import sys
from collections import defaultdict

def parse_log():
    """
    Reads stdin line by line, computes metrics, and prints statistics.
    """
    total_file_size = 0
    status_counts = defaultdict(int)

    try:
        for i, line in enumerate(sys.stdin, start=1):
            ip, _, _, status_code, file_size = line.split(' ')[0], line.split('"')[2].split(' ')[1], line.split('"')[2].split(' ')[2], line.split(' ')[-2], line.split(' ')[-1].strip()

            total_file_size += int(file_size)
            status_counts[status_code] += 1

            if i % 10 == 0:
                print_metrics(total_file_size, status_counts)

    except KeyboardInterrupt:
        print_metrics(total_file_size, status_counts)

def print_metrics(total_file_size, status_counts):
    """
    Prints the computed metrics.

    Args:
        total_file_size (int): The total file size.
        status_counts (dict): The counts of different status codes.
    """
    print("Total file size: File size: {}".format(total_file_size))

    for status_code in sorted(status_counts.keys()):
        count = status_counts[status_code]
        print("{}: {}".format(status_code, count))

    print()

if __name__ == '__main__':
    parse_log()
