# src/get_wp/console.py

import textwrap
import click
import requests
from . import __version__, wikipedia

API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"

@click.command()
@click.version_option(version=__version__)
def main():
    """The get_wp project."""
    data = wikipedia.random_page()
    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))
