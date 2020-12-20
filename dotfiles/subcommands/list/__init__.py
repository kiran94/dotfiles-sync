
from argparse import ArgumentParser, Namespace
import logging
from typing import Dict

from dotfiles.core.matcher import match

COMMAND = "list"

logger = logging.getLogger(__name__)


def add_sub_parser(parser: ArgumentParser):
    _ = parser.add_parser(COMMAND)


def run(config: Dict, args: Namespace):
    logger.info("Listing Configurations")

    matches = match(config, args.config_dir)
    for current_match in matches:
        if args.filter:
            if current_match.key in args.filter:
                logger.info(current_match)
        else:
            logger.info(current_match)
