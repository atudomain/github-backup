import argparse
import sys
import os
from github_backup.backup import do_backup
from contextlib import contextmanager


def cli():
    parser = argparse.ArgumentParser(
        description="Make backup of all github repositories to chosen directory. Pass token and github account as environment variables:\nGITHUB_TOKEN\nGITHUB_USERNAME"
    )
    parser.add_argument(
        "-d", "--directory",
        required=False,
        type=str,
        default=".",
        help="Directory to put backup to."
    )
    args = parser.parse_args()
    directory = args.directory
    prepare_directory(directory)
    with inside_directory(directory):
        do_backup()
    sys.exit(0)


def prepare_directory(directory: str):
    os.makedirs(directory, exist_ok=True)


@contextmanager
def inside_directory(directory):
    old_dir = os.getcwd()
    try:
        os.chdir(directory)
        yield
    finally:
        os.chdir(old_dir)
