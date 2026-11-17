#!/usr/bin/python3
"""Log parsing script: reads stdin line by line and prints metrics
every 10 lines and on keyboard interruption."""
import re
import sys

LINE_RE = re.compile(
    r'^\d{1,3}(?:\.\d{1,3}){3} - \[[^\]]+\] '
    r'"GET /projects/260 HTTP/1\.1" (\S+) (\d+)$'
)
STATUS_CODES = ("200", "301", "400", "401", "403", "404", "405", "500")


def print_stats(total_size, counts):
    """Prints the total file size and the number of lines per status code.

    Args:
        total_size (int): Sum of all file sizes so far.
        counts (dict): Number of lines per status code.
    """
    print("File size: {}".format(total_size))
    for code in sorted(counts):
        print("{}: {}".format(code, counts[code]))


def main():
    """Reads stdin line by line and computes the metrics."""
    total_size = 0
    counts = {}
    line_count = 0

    try:
        for line in sys.stdin:
            match = LINE_RE.match(line.strip())
            if match is None:
                continue

            code, size = match.groups()
            total_size += int(size)
            if code in STATUS_CODES:
                counts[code] = counts.get(code, 0) + 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, counts)
    except KeyboardInterrupt:
        print_stats(total_size, counts)
        raise


if __name__ == "__main__":
    main()
