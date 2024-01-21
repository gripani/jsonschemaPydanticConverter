from argparse import ArgumentParser
from typing import Tuple

from jsonschema_converter.const import PROG_NAME, PROG_DESCRIPTION


def parse_args() -> Tuple[str, str | None]:
    argument_parser = ArgumentParser(
        prog=PROG_NAME,
        description=PROG_DESCRIPTION
    )
    argument_parser.add_argument("--file_name")
    argument_parser.add_argument("--module_name", required=False)
    args = argument_parser.parse_args()
    return args.file_name, args.module_name
