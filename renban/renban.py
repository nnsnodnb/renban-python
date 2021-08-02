import sys
from typing import Optional

import click


@click.command()
@click.option("--prefix", "-p", type=str, default=None)
@click.option("--start-point", "-s", type=int, default=1)
def cmd(prefix: Optional[str], start_point: int) -> None:
    click.echo(prefix)
    click.echo(start_point)


if __name__ == "__main__":
    sys.exit(cmd())
