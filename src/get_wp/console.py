# src/get_wp/console.py
import click

from . import __version__

@click.command()
@click.version_option(version=__version__)
def main():
    """The get_wp project"""
    click.echo("Hulo wurld!")

