import promptlayer
import os
import json
import jinja2

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
Please provide a step-by-step plan that satisfies the following user requirement: "{{ user_requirement }}". Consider the provided protocol descriptions and choose the most suitable protocols and subcontracts to use in each step. Include the necessary ERC20/ERC721 token information if needed.

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
{for protocol in protocols}
- {protocol.name}: {protocol.description}. Supported chains: {', '.join(protocol.supported_chains)}. Subcontracts: {', '.join([subcontract.name for subcontract in protocol.subcontracts])}.
{end}

ERC20/ERC721 Tokens:
{for token in tokens}
- {token.type}: {token.name} ({token.symbol}), Address: {token.address}, Chain: {token.chain}.
{end}
'''

template = jinja2.Template(user_content)
output = template.render(example_input)
print(output)

exit()
openai.ChatCompletion.create(
    model="code-davinci-002",
    messages=[
        {"role": "system", "content": "Create a summary for generating an executable program using the information. Ensure the output includes contract addresses, method signatures, and any necessary additional checks. If any additional checks are needed before performing the actions, include them in the summary."},
        {"role": "user", "content": user_content},

    ],
    pl_tags=["program"]
)
