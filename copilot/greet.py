"""Send greetings."""

import click
import copy
from copilot.pipeline import pipeline
import yaml

import os


@click.command()
@click.option("--input", "-i", type=str)
def run(input):
    pipeline(input)
