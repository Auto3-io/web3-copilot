import promptlayer
import os
import json
import jinja2
from langchain.llms import OpenAI, Anthropic, PromptLayerOpenAI
from langchain.chat_models import PromptLayerChatOpenAI
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.schema import HumanMessage
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

promptlayer.api_key = os.environ['PROMPT_API_KEY']

# Swap out your 'import openai'
openai = promptlayer.openai
openai.api_key = os.environ['OPENAI_API_KEY']

f = open('./example-input.json')
example_input = json.load(f)

user_content = open('./user-content-template.txt').read()

template = jinja2.Template(user_content)
output = template.render(example_input, trim_blocks=True,
                         lstrip_blocks=True, keep_trailing_newline=True, autoescape=False)

user_requirement = example_input['user_requirement']

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
