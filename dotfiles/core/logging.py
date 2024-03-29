import logging
import os

LEVEL = os.environ.get("DOTFILES_LOGGING_LEVEL", "INFO")
FORMAT = os.environ.get("DOTFILES_LOGGING_FORMAT", "%(message)s")
SHOW_PATH = 'SHOW_PATH' in os.environ
SIMPLE_LOGGING = 'DOTFILES_SIMPLE_LOGGING' in os.environ

if SIMPLE_LOGGING:
    from logging import StreamHandler
    handler = StreamHandler()
else:
    from rich.logging import RichHandler
    handler = RichHandler(show_path=SHOW_PATH)

logging.basicConfig(
    level=LEVEL, format=FORMAT, datefmt="[%X]", handlers=[handler]
)
