#!/usr/bin/env python3
import argparse

from gendiff.lib import generate_diff

DEFAULT_FORMAT = "stylish"

parser = argparse.ArgumentParser(
    prog="gendiff",
    description="Compares two configuration files and shows a difference.",
)
parser.add_argument(
    "-f",
    "--format",
    help="set format of output (default: ...)",
    # choices=,
    # default=,
)
parser.add_argument("first_file")
parser.add_argument("second_file")
args = parser.parse_args()


def main():
    diff = generate_diff(args.first_file, args.second_file, DEFAULT_FORMAT)
    print(diff)


if __name__ == "__main__":
    main()
