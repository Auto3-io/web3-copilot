import promptlayer
import os

from copilot.config import PromptLayerChatOpenAI
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from pathlib import Path
import jinja2

from langchain.schema import (
    HumanMessage,
    SystemMessage
)

promptlayer.api_key = os.environ['PROMPT_API_KEY']

# Swap out your 'import openai'
openai = promptlayer.openai
openai.api_key = os.environ['OPENAI_API_KEY']


def program_generator(steps, tokens):
    p = Path(__file__).with_name('./steps_template.txt')
    with p.open('r') as f:
        user_content_template_content = f.read()

    user_template = jinja2.Template(user_content_template_content)
    output = user_template.render(steps=steps, tokens=tokens)

    chat = PromptLayerChatOpenAI(streaming=True, callback_manager=CallbackManager(
        [StreamingStdOutCallbackHandler()]), verbose=True, temperature=0, pl_tags=['program_swap_transfer'])

    messages = [
        SystemMessage(
            content=f'Generate a Python program to accomplish the following on-chain operations:'),
        HumanMessage(
            content=output
        )
    ]
    resp = chat(messages)
    return resp


__all__ = ['program_generator']
