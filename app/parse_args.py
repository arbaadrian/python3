"""
parse args
"""

import argparse
import sys


def _setup_parser():
    """

    Returns:
        (argparse.ArgumentParser): parser for demo rpm
    """
    parser = argparse.ArgumentParser(description="demo rpm")
    parser.add_argument(
        "name",
        help="package to look for"
    )
    parser.add_argument(
        "version",
        help="package version to look for",
        default=None,
        nargs='?'
    )
    return parser


def get_program_args():
    """

    Returns:
        (dict): command line args
    """
    parser = _setup_parser()
    program_args = parser.parse_args(sys.argv[1:])

    return program_args
