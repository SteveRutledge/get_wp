# src/get_wp/console.py

import textwrap
import click
from . import __version__, wikipedia

@click.command()
@click.option(
        "--language",
        "-l",
        default="en",
        help="language edition of Wikipedia",
        metavar="LANG",
        show_default=True,
        )
@click.version_option(version=__version__)
def main(language):
    """The get_wp project."""
    data = wikipedia.random_page(language=language)
    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
