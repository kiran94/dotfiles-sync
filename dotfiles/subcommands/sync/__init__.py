
from argparse import ArgumentParser, Namespace
import logging
from typing import Dict

COMMAND = "sync"

logger = logging.getLogger(__name__)

def add_sub_parser(parser: ArgumentParser):
    sub = parser.add_parser(COMMAND)

def run(config: Dict, args: Namespace):
    print('running sync')
    pass