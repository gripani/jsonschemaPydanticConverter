from argparse import ArgumentParser
from typing import Tuple

from jsonschema_converter.const import PROG_NAME, PROG_DESCRIPTION


def on_error(parser: ArgumentParser):
    def wrapper(interceptor):
        parser.print_help()
        exit(-1)
    return wrapper


def parse_args() -> Tuple[str, str, str]:
    argument_parser = ArgumentParser(
        prog=PROG_NAME,
        description=PROG_DESCRIPTION
    )
    argument_parser.error = on_error(argument_parser)
    argument_parser.add_argument("-f", "--file_name",
                                 required=True,
                                 help="jsonschema file name")
    argument_parser.add_argument("-m", "--module_name",
                                 required=False,
                                 help="module directory to save classes (default: schemas)",
                                 default="schemas")
    argument_parser.add_argument("-l", "--log_level",
                                 required=False,
                                 help="logging level: ERROR, WARNING, DEBUG, INFO (default: ERROR)",
                                 default="ERROR")
    args = argument_parser.parse_args()
    return args.file_name, args.module_name, args.log_level
