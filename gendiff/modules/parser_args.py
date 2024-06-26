import argparse


def parser_args():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", help="first file")
    parser.add_argument("second_file", help="second file")
    parser.add_argument(
        "-f",
        "--format",
        help="set format of output",
        default="stylish",
        choices=["stylish", "plain", "json"],
    )
    args = parser.parse_args()
    return args
