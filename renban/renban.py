import os
import sys
from pathlib import Path
from typing import Optional, Tuple

import click


@click.command()
@click.option('--prefix', "-p", type=str, default=None)
@click.option("--start-point", "-s", type=int, default=1)
@click.option("--input-path", "-i", type=str, default="./")
@click.option("--output-path", "-o", type=str, default="./outputs")
@click.option("--excludes", "-e", multiple=True)
@click.option("--verbose", "-v", is_flag=True)
def cmd(
    prefix: Optional[str], start_point: int, input_path: str, output_path: str, excludes: Tuple[str], verbose: bool
) -> None:
    _input_path = Path(input_path)
    files = [f for f in _input_path.iterdir() if f.is_file() and f.name not in excludes]

    _output_path = Path(output_path)
    _output_path.mkdir(exist_ok=True)

    _prefix = f"{prefix}_" if prefix is not None else ""
    for idx, f in enumerate(files):
        suffixes = "".join(f.suffixes)
        target = _output_path / f"{_prefix}{start_point + idx}{suffixes}"
        f.rename(target)
        if verbose:
            click.echo(f"Move: {f.absolute()} -> {target.absolute()}")


if __name__ == "__main__":
    sys.exit(cmd())
