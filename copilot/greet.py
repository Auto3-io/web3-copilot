"""Send greetings."""

import click
import copy
from copilot.task_interpreter.task_interpreter import task_interpreter
from copilot.method_search_engine.engine import search_engine
from copilot.data.loader import get_contract_address, get_erc20_address
from copilot.program_generator.program import program_generator
import yaml

import os
import ipdb


@click.command()
@click.option("--input", "-i", type=str)
def run(input):
    click.echo('Strat interpreter user task: {}'.format(input))
    steps_raw = task_interpreter(input)
    ipdb.set_trace()
    steps = yaml.safe_load(steps_raw.content)['steps']

    tokens = {}
    for step in steps:
        if 'tokens' in step:
            for token in step['tokens']:
                if token['name'] not in tokens:
                    tokens[token['name']] = get_erc20_address(
                        str(token['name']).upper(), str(token['chain']).lower())

    transformed_tokens = []
    for token in tokens:
        transformed_tokens.append(
            {'name': token['symbol'], 'chain': token['chain'], 'address': token['address']})

    for step in steps:
        if not step['action']:
            raise Exception("No action in step: {}".format(step))

    click.echo('Start searching methods: {}'.format(
        [step['action'] for step in steps]))
    summarized_steps = search_engine([step['action'] for step in steps])

    if len(steps) != len(summarized_steps):
        raise Exception("Step count not match")

    to_program_steps = []
    for i in range(summarized_steps):
        new_step = copy.deepcopy(summarized_steps[i])
        new_step['action'] = steps[i]['action']
        new_step['protocol'] = summarized_steps[i]['protocol']
        new_step['contract'] = summarized_steps[i]['contract']
        new_step['chain'] = summarized_steps[i]['chain']

        print("Find contract address: {} {} {}".format(
            new_step['protocol'], new_step['contract'], new_step['chain']))

        new_step['address'] = get_contract_address(
            new_step['protocol'], new_step['chain'], new_step['contract'])
        to_program_steps.append(new_step)

    program = program_generator(to_program_steps, )

    # save program to local tmp dir
    file_path = os.path.join('./', 'code.py')
    with open(file_path, 'w') as file:
        file.write(program)
