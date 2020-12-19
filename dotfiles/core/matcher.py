import os
import logging
from enum import Enum
from typing import Dict, Iterable

from rich.progress import track

from dotfiles import OPERATING_SYSTEM, PROGRESS_BAR_THRESHOLD

logger = logging.getLogger(__name__)


class ConfigurationMatchStatus(Enum):
    UNKNOWN = 0,
    SYNCHRONIZABLE = 1
    MISSING_OPERATING_SYSTEM_CONFIG = 2
    MISSING_SOURCE_FILE = 3


class ConfigurationFileType(Enum):
    UNKNOWN = 0
    FILE = 1
    DIRECTORY = 2


class ConfigurationMatch:
    '''
    Represents a match between the source and target configurations and provides the status.
    '''

    def __init__(self, key: str, source: str, target: str, status: ConfigurationMatchStatus) -> None:
        self.key: str = key
        self.source: str = os.path.expanduser(source)
        self.target: str = os.path.expanduser(target)
        self.status: ConfigurationMatchStatus = status

        if not self.source:
            self.source_type = ConfigurationFileType.UNKNOWN

        elif os.path.exists(self.source) and os.path.isdir(self.source):
            self.source_type = ConfigurationFileType.DIRECTORY

        elif os.path.exists(self.source) and os.path.isfile(self.source):
            self.source_type = ConfigurationFileType.FILE

        elif os.path.exists(self.target) and os.path.isdir(self.target):
            self.source_type = ConfigurationFileType.DIRECTORY

        elif os.path.exists(self.target) and os.path.isfile(self.target):
            self.source_type = ConfigurationFileType.FILE

        else:
            self.source_type = ConfigurationFileType.UNKNOWN

    def __str__(self) -> str:
        return f'{self.key}: {self.source} => {self.target} ({self.status} | {self.source_type})'


def match(config: Dict, configuration_source_file_dir: str, hide_progress: bool = False) -> Iterable[ConfigurationMatch]:
    '''
    Matches the Configuration File with the Source Files vs the Files on the System
    '''
    configuations = config['config']
    configuations_directory = configuration_source_file_dir

    source_files = os.listdir(configuations_directory)
    source_files = {s: os.path.join(configuations_directory, s)
                    for s in source_files}

    hide_progress = not (len(configuations) >
                         PROGRESS_BAR_THRESHOLD) or hide_progress

    for config_key in track(configuations.keys(), description='Processing...', disable=hide_progress):
        status = ConfigurationMatchStatus.SYNCHRONIZABLE

        '''
        The Configuration file did not have a value for this config_key for this operating system
        '''
        try:
            target_configuration = configuations[config_key][OPERATING_SYSTEM]
        except KeyError:
            logger.warning('%s did not have a configuration for %s',
                           config_key, OPERATING_SYSTEM)
            status = ConfigurationMatchStatus.MISSING_OPERATING_SYSTEM_CONFIG
            target_configuration = None

        '''
        The source files did not exist for this key in the configuration
        '''
        try:
            source_configuation = source_files[config_key]
        except KeyError:
            logger.warning('%s was found in config but does not exist in source %s',
                           config_key, configuration_source_file_dir)
            status = ConfigurationMatchStatus.MISSING_SOURCE_FILE
            source_configuation = os.path.join(
                configuations_directory, config_key)

        c = ConfigurationMatch(
            config_key, source_configuation, target_configuration, status)
        yield c
