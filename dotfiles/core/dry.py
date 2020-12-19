import logging
from typing import Callable

from rich.console import Console

console = Console()

logger = logging.getLogger(__name__)


def call(func: Callable, dry: bool, interactive: bool, *args, **kwargs):
    if dry:
        logger.warning('Skipping as dry run option was set')
    else:

        if interactive:
            res = input(f'About to run {func.__name__} {args} {kwargs} Are you sure? (Y, N)')
            logger.debug(f'Input from interactive {res}')
            if str.upper(res) == "Y":
                func(*args, **kwargs)
            else:
                logger.info('Skipping...')
        else:
            func(*args, **kwargs)
