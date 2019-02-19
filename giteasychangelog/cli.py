# -*- coding: utf-8 -*-

"""Console script for giteasychangelog."""
import sys
import click

import giteasychangelog.giteasychangelog as changelog


@click.command()
def main(args=None):
    """Console script for giteasychangelog."""
    # TODO CONTROL ARGS

    changelog.main(args)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
