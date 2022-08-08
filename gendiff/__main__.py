#!/usr/bin/env python3
import argparse

from gendiff.generate_diff import generate_diff

DEFAULT_FORMAT = "stylish"

FORMATS = ["stylish", "plain", "json"]

parser = argparse.ArgumentParser(
    prog="gendiff",
    description="Compares two configuration files and shows a difference.",
)
parser.add_argument(
    "-f",
    "--format",
    help=f"set format of output (default: {DEFAULT_FORMAT})",
    choices=FORMATS,
    default=DEFAULT_FORMAT,
)
parser.add_argument("first_file")
parser.add_argument("second_file")
args = parser.parse_args()


def main():
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()
