from .. import config
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


p = Path(__file__).with_name('data.json')
with p.open('r') as f:
    protocol_data = f.read()


def task_interpreter(steps):
    user_content_template_content = open('./user-content-template.txt').read()

    user_template = jinja2.Template(user_content_template_content)
    output = user_template.render(protocol_data, trim_blocks=True,
                                  lstrip_blocks=True, keep_trailing_newline=True, autoescape=False)

    chat = PromptLayerChatOpenAI(streaming=True, callback_manager=CallbackManager(
        [StreamingStdOutCallbackHandler()]), verbose=True, temperature=0, pl_tags=['summarizer'])

    messages = [
        SystemMessage(
            content='Summarize the following steps for generating an executable Web3 program. For each step, include the description, contract address, method name, associated contract, protocol, and a brief description of the method.'),
        HumanMessage(
            content=output
        )
    ]
    resp = chat(messages)

    return resp
