"""Send greetings."""

import time

import arrow
import click
from prompt.task_interpreter import task_interpreter


@click.command()
@click.argument("tz")
@click.option("--repeat", "-r", default=1, type=int)
@click.option("--interval", "-i", default=3, type=int)
def copilot(tz, repeat=1, interval=3):
    overall_steps = task_interpreter(user_requirement) # Step with protocol, chain
    search_result = method_search_engine(overall_steps, db.methods) # + contract, method

    completed_steps = complete_step(search_result, db.contracts, db.tokens) # + address
    summarized_steps = summarizer(user_requirement, search_result) # summrize

    program = program_generator(summarized_steps)