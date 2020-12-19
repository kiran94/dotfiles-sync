import logging
from typing import Callable

logger = logging.getLogger(__name__)

def call(func: Callable, dry: bool, *args, **kwargs):
    if dry:
        logger.warning('Skipping as dry run option was set')
    else:
        func(*args, **kwargs)
        