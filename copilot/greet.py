"""Send greetings."""

import click
from copilot.pipeline import pipeline


@click.command()
@click.option("--input", "-i", type=str)
def run(input):
    pipeline(input)
