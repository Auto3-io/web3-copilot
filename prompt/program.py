import promptlayer
import os
promptlayer.api_key = os.environ['PROMPT_API_KEY']

# Swap out your 'import openai'
openai = promptlayer.openai
openai.api_key = os.environ['OPENAI_API_KEY']

# Do something fun 🚀
openai.Completion.create(
    engine="text-ada-001",
    prompt="My name is",
    pl_tags=["name-guessing", "pipeline-2"]
)

# exit()

user_content = '''
1. Swap 1000 USDC for ETH using Uniswap on Ethereum:
- Contract address: 0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D
- Method: swapExactTokensForTokens
- ABI: '{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"}'
- Documentation: Swaps an exact amount of input tokens for as many output tokens as possible...
- Additional check: allowance
  - ABI: {...}
  - Documentation: Returns the remaining number of tokens that spender will be allowed to spend on behalf of owner...
- Additional action: approve
  - ABI: {...}
  - Documentation: Approves a specified address to spend a specified amount of tokens on the caller's behalf...

2. Send half of the acquired ETH to 0x123:
- Contract address: 0xETH...
- Method: transfer
- ABI: {...}
- Documentation: Transfers tokens from the sender's account to the specified address...

3. Deposit the rest of the ETH to Aave:
- Contract address: 0x67890...
- Method: deposit
- ABI: '{"anonymous":false,"inputs":[{"indexed":false,"name":"_reserve","type":"address"},{"indexed":false,"name":"_user","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"}],"name":"Deposit","type":"event","signature":"0x5548c837ab068cf56a2c2479df0882a4922fd203edb7517321831d95078c5f62"}'
- Documentation: Deposits an asset into the protocol to start earning interest...
- Additional check: allowance
  - ABI: {...}
  - Documentation: Returns the remaining number of tokens that
- Additional action: approve
  - ABI: {...}
  - Documentation: Approves a specified address to spend a specified amount of tokens on the caller's behalf...

Related ERC20:
1. USDC
- Address: 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48
'''


openai.ChatCompletion.create(
    model="code-davinci-002",
    messages=[
        {"role": "system", "content": "Generate a Python program to accomplish the following on-chain operations:"},
        {"role": "user", "content":  user_content},
    ],
    pl_tags=["program"]
)
