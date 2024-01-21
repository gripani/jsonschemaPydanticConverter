from argparse import ArgumentParser
from typing import Tuple

from jsonschema_converter.const import PROG_NAME, PROG_DESCRIPTION


def on_error(parser: ArgumentParser):
    def wrapper(interceptor):
        parser.print_help()
        exit(-1)
    return wrapper


def parse_args() -> Tuple[str, str | None]:
    argument_parser = ArgumentParser(
        prog=PROG_NAME,
        description=PROG_DESCRIPTION
    )
    argument_parser.error = on_error(argument_parser)
    argument_parser.add_argument("--file_name", required=True)
    argument_parser.add_argument("--module_name", required=False)
    args = argument_parser.parse_args()
    return args.file_name, args.module_name
