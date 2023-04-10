from copilot.config import ChatOpenAI
from copilot.data.loader import get_protocols
import jinja2
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.schema import HumanMessage
from pathlib import Path


from langchain.schema import (
    HumanMessage,
    SystemMessage
)

protocols = get_protocols()


def task_interpreter(user_requirement: str):
    p = Path(__file__).with_name('./interpreter-input-template.txt')
    with p.open('r') as f:
        user_content_template_content = f.read()

    user_template = jinja2.Template(user_content_template_content)
    output = user_template.render(protocols=protocols)

    chat = ChatOpenAI(streaming=True, callback_manager=CallbackManager(
        [StreamingStdOutCallbackHandler()]), verbose=True, temperature=0, pl_tags=['task interpreter'])

    system_instruction = (
        f"Please provide a step-by-step plan that satisfies the following user requirement: {user_requirement}"
        "Consider the provided protocol descriptions and choose the most suitable protocols and subcontracts to use in each step. "
        "Include the necessary ERC20/ERC721 token information if needed. "
        "The source of assets for each step of operation should also be clearly explained, "
        "such as the result from a specific step or from user\'s balance.\n\n"
        "Requirements:\n"
        "  1. As few steps as possible. \n"
        "  2. There is no need to list delegate or approve authorization as a separate step;"
        "  simply add requirement of `delegate` or `approve` operation if needed to the notes."
        "  Specify whether it is necessary to check beforehand, such as the need to verify"
        "  the allowance before using many tokens. For example, a swap only need output one step."
    )
    messages = [
        SystemMessage(
            content=system_instruction),
        HumanMessage(
            content=output
        )
    ]
    resp = chat(messages)

    return resp
