
from argparse import ArgumentParser, Namespace
import logging
from typing import Dict
from shutil import copyfile
from distutils.dir_util import copy_tree

from rich.progress import track

from dotfiles.core.dry import call
from dotfiles.core.matcher import match, ConfigurationFileType

COMMAND = "sync"

logger = logging.getLogger(__name__)

def add_sub_parser(parser: ArgumentParser):
    _ = parser.add_parser(COMMAND)

def run(config: Dict, args: Namespace):

    config_dir = args.config_dir
    matches = list(match(config, config_dir, hide_progress=True))

    for config in track(matches, description=f'Syncing Configuration...'):

        if config.source_type == ConfigurationFileType.FILE:
            logger.info('Copying File %s => %s', config.source, config.target)
            call(copyfile, args.dry, config.source, config.target)

        elif config.source_type == ConfigurationFileType.DIRECTORY:
            logger.info('Copying Directory %s => %s', config.source, config.target)
            call(copy_tree, args.dry, config.source, config.target)