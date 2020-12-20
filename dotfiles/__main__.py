import argparse
import logging
import json
from typing import Dict

from dotfiles import __version__
import dotfiles.core.logging
import dotfiles.subcommands.list
import dotfiles.subcommands.sync
import dotfiles.subcommands.update

logger = logging.getLogger("dotfiles")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', default='dotfiles-sync.json', help='dotfiles configuration. Points to target locations.')
    parser.add_argument('-w', '--config_dir', default='.', help='Location of the configuration files to sync')
    parser.add_argument('-d', '--dry', action='store_true', default=False, help='Only read and show me what you would have done')
    parser.add_argument('-i', '--interactive', action='store_true', default=False, help='Before doing a write, ask for confirmation')
    parser.add_argument('-f', '--filter', nargs='+', default=[], help='keys(s) of the configuration to apply. If not set then apply them all')
    parser.add_argument('--version', action='version', version=__version__)

    sub_parsers = parser.add_subparsers(dest='command')
    dotfiles.subcommands.list.add_sub_parser(sub_parsers)
    dotfiles.subcommands.sync.add_sub_parser(sub_parsers)
    dotfiles.subcommands.update.add_sub_parser(sub_parsers)

    args = parser.parse_args()

    with open(args.config) as c:
        config: Dict = json.load(c)

    if args.command == dotfiles.subcommands.list.COMMAND:
        dotfiles.subcommands.list.run(config, args)
    elif args.command == dotfiles.subcommands.sync.COMMAND:
        dotfiles.subcommands.sync.run(config, args)
    elif args.command == dotfiles.subcommands.update.COMMAND:
        dotfiles.subcommands.update.run(config, args)
    else:
        raise ValueError('Unknown Command')


if __name__ == "__main__":
    main()
