import platform
import os

OPERATING_SYSTEM: str = platform.system().lower()
PROGRESS_BAR_THRESHOLD: int = int(os.environ.get('PROGRESS_BAR_THRESHOLD', 5))

__version__ = '0.0.10'
