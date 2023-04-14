import click
import yaml

from copilot.data.loader import get_contract_address, get_erc20_address
from copilot.method_search_engine.engine import search_engine
from copilot.program_generator.program import program_generator
from copilot.task_interpreter.task_interpreter import task_interpreter


def pipeline(input):
    click.echo('Strat interpreter user task: {}'.format(input))
    steps_raw = task_interpreter(input)
    steps = yaml.safe_load(steps_raw.content)['steps']

    tokens = {}
    tokens = {
        token_name: token_address
        for step in steps
        for token_name, token_address in get_tokens_from_step(step, tokens).items()
    }

    for step in steps:
        if not step['action']:
            raise Exception("No action in step: {}".format(step))

    click.echo('\nStart searching methods: {}'.format(
        [step['action'] for step in steps]))
    summarized_steps = search_engine([step['action'] for step in steps])
    click.echo('\nFinish searching methods')

    if len(steps) != len(summarized_steps):
        raise Exception("Step count not match")

    to_program_steps = []
    for i in range(len(summarized_steps)):
        raw_step = summarized_steps[i].response
        print('\n Step {}:\n {}'.format(i, raw_step))

        new_step = yaml.safe_load((raw_step))
        new_step['action'] = steps[i]['action']
        for method in new_step['methods']:
            for contract in method['needed_contracts']:
                contract['address'] = get_contract_address(
                    contract['protocol'], contract['chain'], contract['contract'])
                print("Find contract address: {}:{}({}), {} \n".format(
                    contract['protocol'], contract['contract'], contract['chain'], contract['address']))
        to_program_steps.append(new_step)

    program = program_generator(to_program_steps, tokens)
    return program

    # TODO: save an run on vm
    # file_path = os.path.join('./', 'tmp_code.py')
    # with open(file_path, 'w') as file:
        # file.write(program.content)


def get_tokens_from_step(step, tokens):
    if 'tokens' in step:
        return {
            token['name']: get_erc20_address(
                str(token['name']).upper(), str(token['chain']).lower()
            )
            for token in step['tokens'] if token['name'] not in tokens
        }
    return {}
