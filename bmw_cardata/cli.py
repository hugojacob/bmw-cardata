"""
Command line interface for BMW CarData.
"""
import argparse
import pathlib


def get_arg_parser() -> argparse.ArgumentParser:
    """
    Get the argument parser.
    """
    arg_parser = argparse.ArgumentParser(
        description=(
            "CLI tool to parse BMW CarData charging history and generate HTML reports."
        )
    )
    arg_parser.add_argument(
        "--locations",
        default=None,
        help="YAML file with the known locations",
    )
    arg_parser.add_argument(
        "file",
        nargs="+",
        type=pathlib.Path,
        help="Charging history JSON file from BMW CarData",
    )
    return arg_parser


def main():
    """
    Command line interface entrypoint.
    """
    get_arg_parser().parse_args()
