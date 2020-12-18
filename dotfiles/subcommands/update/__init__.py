
from argparse import ArgumentParser, Namespace
import logging
from typing import Dict
from shutil import copyfile

from rich.progress import track

from dotfiles import FOLLOW_SYMLINKS
from dotfiles.core.matcher import match, ConfigurationFileType

COMMAND = "update"

logger = logging.getLogger(__name__)

def add_sub_parser(parser: ArgumentParser):
    _ = parser.add_parser(COMMAND)

def run(config: Dict, args: Namespace):

    config_dir = args.config_dir
    matches = list(match(config, config_dir, hide_progress=True))

    for config in track(matches, description=f'Updating Configuration Directory: {config_dir}'):

        if config.source_type == ConfigurationFileType.FILE:
            logger.info('Copying %s => %s', config.target, config.source)
            copyfile(config.target, config.source, follow_symlinks=FOLLOW_SYMLINKS)

        elif config.source == ConfigurationFileType.DIRECTORY:
            pass
