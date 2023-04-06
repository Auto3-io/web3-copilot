import promptlayer
import os
import json
import jinja2
from langchain.llms import OpenAI, Anthropic
from langchain.chat_models import ChatOpenAI
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.schema import HumanMessage

llm = OpenAI(streaming=True, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]), verbose=True, temperature=0)
resp = llm("Write me a song about sparkling water.")

exit()
promptlayer.api_key = os.environ['PROMPT_API_KEY']

# Swap out your 'import openai'
openai = promptlayer.openai
openai.api_key = os.environ['OPENAI_API_KEY']

f = open('./example-input.json')
example_input = json.load(f)

"""
- user_requrement
- protocols: list
    - name
    - description
    - supported_chains: list
    - subcontracts: list
        - name
        - address
        - description
- tokens: list
    - name
    - type
    - symbol
    - chains
        - name
        - address
"""

user_content = '''
The output schema must be:
- steps: list
    - step_number
    - action
    - protocol (if needed)
        - name
        - description
        - supported_chains
        - subcontract
            - name
            - address
            - description
Protocol Descriptions:
{% for protocol in protocols -%}
- {{ protocol.name }}: {{ protocol.description }}. 
    Supported chains: {{ ', '.join(protocol.supported_chains) }}. 
    Subcontracts:
    {% for subcontract in protocol.subcontracts -%}
        - {{ subcontract.name }}: {{ subcontract.description }}
        {% for chain in subcontract.chains -%}
        - {{ chain.name }}: {{ chain.address }}
        {% endfor -%}
    {% endfor -%}
{% endfor -%}

ERC20/ERC721 Tokens:
{% for token in tokens -%}
- {{ token.type }}: {{ token.name }} ({{ token.symbol }})
    {% for chain in token.chains -%}
    - Address: {{chain.address}}, Chain: {{chain.name}}
    {% endfor -%}
{% endfor -%}
'''

template = jinja2.Template(user_content)
output = template.render(example_input, trim_blocks=True,
                         lstrip_blocks=True, keep_trailing_newline=True, autoescape=False)

user_requirement = example_input['user_requirement']
openai.ChatCompletion.create(
    model="code-davinci-002",
    messages=[
        {"role": "system", "content": f'Please provide a step-by-step plan that satisfies the following user requirement "{user_requirement}". Consider the provided protocol descriptions and choose the most suitable protocols and subcontracts to use in each step. Include the necessary ERC20/ERC721 token information if needed.'},
        {"role": "user", "content": output},

    ],
    pl_tags=["keyword"]
)
