#!/usr/bin/python3
"""
Log parsing
"""

import sys

def print_stats(status_counts, total_file_size):
    """ Prints a message with the stats """
    print(f"File size: {total_file_size}")
    for code, count in sorted(status_counts.items()):
        if count != 0:
            print(f"{code}: {count}")

def process_line(line, status_counts, total_file_size):
    parsed_line = line.split()
    if len(parsed_line) >= 3:
        status_code = parsed_line[-2]
        file_size = int(parsed_line[-1])
        status_counts[status_code] += 1
        total_file_size += file_size
    return status_counts, total_file_size

status_counts = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
total_file_size = 0
counter = 0

try:
    for line in sys.stdin:
        status_counts, total_file_size = process_line(line.strip(), status_counts, total_file_size)
        counter += 1
        """if counter == 10:
            print_stats(status_counts, total_file_size)
            counter = 0
"""
finally:
    print_stats(status_counts, total_file_size)

