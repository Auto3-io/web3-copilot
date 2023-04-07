import promptlayer
import os
import json
import jinja2
from langchain.chat_models import PromptLayerChatOpenAI
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.schema import HumanMessage
from pathlib import Path


from langchain.schema import (
    HumanMessage,
    SystemMessage
)

promptlayer.api_key = os.environ['PROMPT_API_KEY']
openai = promptlayer.openai
openai.api_key = os.environ['OPENAI_API_KEY']

p = Path(__file__).with_name('data.json')
with p.open('r') as f:
    protocol_data = f.read()


def task_interpreter(user_requirement: str):
    user_content_template_content = open('./user-content-template.txt').read()

    user_template = jinja2.Template(user_content_template_content)
    output = user_template.render(protocol_data, trim_blocks=True,
                                  lstrip_blocks=True, keep_trailing_newline=True, autoescape=False)

    chat = PromptLayerChatOpenAI(streaming=True, callback_manager=CallbackManager(
        [StreamingStdOutCallbackHandler()]), verbose=True, temperature=0, pl_tags=['task interpreter'])

    messages = [
        SystemMessage(
            content=f'Please provide a step-by-step plan that satisfies the following user requirement "{user_requirement}". Consider the provided protocol descriptions and choose the most suitable protocols and subcontracts to use in each step. Include the necessary ERC20/ERC721 token information if needed. The source of assets for each step of operation should also be clearly explained, such as the result from a specific step or from user\'s balance.'),
        HumanMessage(
            content=output
        )
    ]
    resp = chat(messages)

    return resp
