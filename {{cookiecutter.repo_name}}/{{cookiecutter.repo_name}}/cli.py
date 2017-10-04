#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
{{cookiecutter.repo_name}}
===

A advance cli-based python program named {{cookiecutter.repo_name}}
"""

# python std library
import logging
import logging.config
import sys
from pprint import pformat

# {{cookiecutter.repo_name}} imports

# 3rd party imports
from docopt import docopt

log = None

base_args = """
Usage:
    {{cookiecutter.repo_name}} [-v ...] [options] <command> [<args> ...]

Available {{cookiecutter.repo_name}} commands are:
    test                Test command

Options:
    -h, --help          Show this help message and exit
    -q, --quiet         Suppress terminal output
    -v, --verbose       Verbose terminal output (multile -v increses verbosity)
    -V, --version       Display the version number and exit
    --haste             Post the logfile to hastebin server
    """

test_args = """
Usage:
    {{cookiecutter.repo_name}} test [options]

Options:
    -h, --help          Show this help message and exit
    -q, --quiet         Suppress terminal output
"""

def parse_cli():
    """
    Split the functionality into two methos.

    One for parsing the cli and one that runs the application.
    """
    import {{cookiecutter.repo_name}}

    global log

    from docopt import extras, Option, DocoptExit

    try:
        cli_args = docopt(base_args, options_first=True,
                          version={{cookiecutter.repo_name}}.__version__,
                          help=True)
    except DocoptExit:
        extras(True, {{cookiecutter.repo_name}}.__version__,
               [Option('-h', '--help', 0, True)], base_args)

    argv = [cli_args['<command>']] + cli_args['<args>']

    {{cookiecutter.repo_name}}.init_logging(
        1 if cli_args["--quiet"] else cli_args["--verbose"])

    log = logging.getLogger(__name__)
    log.debug(sys.argv)
    log.debug("Setting verbose level: {0}".format(cli_args["--verbose"]))
    log.debug("Arguments from CLI: \n{0}".format(pformat(cli_args)))

    if cli_args['<command>'] == 'test':
        sub_args = docopt(eval('{sub}_args'.format(
            sub=cli_args['<command>'])), argv=argv)
    else:
        extras(True, {{cookiecutter.repo_name}}.__version__,
               [Option('-h', '--help', 0, True)], base_args)
        sys.exit(1)

    if len(cli_args['<args>']) > 0:
        sub_args['<sub_command>'] = cli_args['<args>'][0]
        log.debug("Sub arguments from CLI: \n{0}".format(pformat(sub_args)))

    return (cli_args, sub_args)


def run(cli_args, sub_args):
    if cli_args['<command>'] == 'test':
        log.info("Running test function")
    else:
        log.debug("Command not implemented")


def cli_entrypoint():
    """
    Used by setup.py to create a cli entrypoint script
    """

    cli_args, sub_args = parse_cli()

    try:
        run(cli_args, sub_args)
    except Exception:
        raise
    finally:
        import {{cookiecutter.repo_name}}
        global log

        log.debug("All logging can be found in file: {log}".format(
            log={{cookiecutter.repo_name}}.random_log_file))
