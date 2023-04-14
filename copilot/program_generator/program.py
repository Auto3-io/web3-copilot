import promptlayer
import os

from copilot.config import ChatOpenAI
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from pathlib import Path
import jinja2

from langchain.schema import (
    HumanMessage,
    SystemMessage
)


def program_generator(steps, tokens):
    p = Path(__file__).with_name('./steps_template.txt')
    with p.open('r') as f:
        user_content_template_content = f.read()

    user_template = jinja2.Template(user_content_template_content)
    output = user_template.render(steps=steps, tokens=tokens)

    chat_args = {'streaming': True, 'callback_manager': CallbackManager([StreamingStdOutCallbackHandler()]), 'verbose': True, 'temperature': 0}

    if os.getenv('PROMPTLAYER_API_KEY') is not None:
        chat_args['pl_tags'] = ['program_generator']

    chat = ChatOpenAI(**chat_args)

    print("\nProgram instructions: \n")
    print(output)

    messages = [
        SystemMessage(
            content=f'Generate a Python PROGRAM to accomplish the following on-chain operations: (Do not include any additional information besides program.)'),
        HumanMessage(
            content=output
        )
    ]
    resp = chat(messages)
    return resp


__all__ = ['program_generator']
