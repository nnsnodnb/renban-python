import sys
from pathlib import Path
from typing import Tuple, Optional

import click


@click.command()
@click.option("--prefix", "-p", type=str, default=None)
@click.option("--start-point", "-s", type=int, default=1)
@click.option("--input-path", "-i", type=str, default="./")
@click.option("--excludes", "-e", multiple=True)
def cmd(prefix: Optional[str], start_point: int, input_path: str, excludes: Tuple[str]) -> None:
    _input_path = Path(input_path)
    files = [f for f in _input_path.iterdir() if f.is_file() and f.name not in excludes]


if __name__ == "__main__":
    sys.exit(cmd())
