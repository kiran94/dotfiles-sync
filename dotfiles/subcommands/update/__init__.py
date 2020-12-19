
import os
import logging
from argparse import ArgumentParser, Namespace
from typing import Dict
from shutil import copyfile
from distutils.dir_util import copy_tree

from rich.progress import track

from dotfiles.core.dry import call
from dotfiles.core.matcher import match, ConfigurationFileType

COMMAND = "update"

logger = logging.getLogger(__name__)


def add_sub_parser(parser: ArgumentParser):
    _ = parser.add_parser(COMMAND)


def run(config: Dict, args: Namespace):

    config_dir = args.config_dir
    matches = list(match(config, config_dir, hide_progress=True))
    hide_progress = args.dry or args.interactive

    for config in track(matches, description=f'Updating Configuration Directory: {config_dir}', disable=hide_progress):

        if config.source_type == ConfigurationFileType.FILE:
            logger.info('Copying File %s => %s', config.target, config.source)

            directory = os.path.dirname(config.source)
            call(os.makedirs, args.dry, args.interactive, directory, exist_ok=True)
            call(copyfile, args.dry, args.interactive, config.target, config.source)

        elif config.source_type == ConfigurationFileType.DIRECTORY:
            logger.info('Copying Directory %s => %s', config.target, config.source)
            call(copy_tree, args.dry, args.interactive, config.target, config.source)
