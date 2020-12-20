
from argparse import ArgumentParser, Namespace
import logging
import os
from typing import Dict
from shutil import copyfile
from distutils.dir_util import copy_tree

from rich.progress import track

from dotfiles.core.dry import call
from dotfiles.core.matcher import ConfigurationMatchStatus, match, ConfigurationFileType

COMMAND = "sync"
ALLOWED_MATCH_STATUSES = [ConfigurationMatchStatus.SYNCHRONIZABLE]

logger = logging.getLogger(__name__)


def add_sub_parser(parser: ArgumentParser):
    _ = parser.add_parser(COMMAND)


def run(config: Dict, args: Namespace):

    config_dir = args.config_dir
    matches = list(match(config, config_dir, hide_progress=True))
    hide_progress = args.dry or args.interactive

    for config in track(matches, description='Syncing Configuration...', disable=hide_progress):

        if config.status not in ALLOWED_MATCH_STATUSES:
            logger.warning('%s had status %s. Skipping.', config.key, config.status)
            continue

        if config.disabled:
            logger.warning('%s is disabled. Skipping.', config.key)
            continue

        if args.filter and (config.key not in args.filter):
            logger.debug('%s is not in explicit filter list %s. Skipping.', config.key, args.filter)
            continue

        if config.source_type == ConfigurationFileType.FILE:
            logger.info('Copying File %s => %s', config.source, config.target)
            directory = os.path.dirname(config.target)
            call(os.makedirs, args.dry, args.interactive, directory, exist_ok=True)
            call(copyfile, args.dry, args.interactive, config.source, config.target)

        elif config.source_type == ConfigurationFileType.DIRECTORY:
            logger.info('Copying Directory %s => %s', config.source, config.target)
            call(copy_tree, args.dry, args.interactive, config.source, config.target)
