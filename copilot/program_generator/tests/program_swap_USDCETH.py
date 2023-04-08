import promptlayer
import os
promptlayer.api_key = os.environ['PROMPT_API_KEY']

# Swap out your 'import openai'
openai = promptlayer.openai
openai.api_key = os.environ['OPENAI_API_KEY']

user_content = '''
1. Swap 1000 USDC for ETH using Uniswap on Ethereum:
- Contract address: 0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D
- Method: swapExactTokensForETH
- ABI: '[{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"}]'
- Documentation: Swaps an exact amount of input tokens for as many output tokens as possible...
- Additional check: allowance
  - ABI: '[{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]'
  - Documentation: Returns the remaining number of tokens that spender will be allowed to spend on behalf of owner...
- Additional action: approve
  - ABI: '[{"constant":false,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
  - Documentation: Approves a specified address to spend a specified amount of tokens on the caller's behalf...

Related ERC20:
1. USDC (0x65aFADD39029741B3b8f0756952C74678c9cEC93)
2. WETH (0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6)

Note: 
- the path from USDC to ETH is [USDC, WETH]
- "nonce": w3.eth.getTransactionCount(account.address)
- gas_price = w3.toWei("300", "gwei")
- if token_amount needed, decimals = token_in.functions.decimals().call(), and token_amount_in_wei = int(amount * (10**decimals)) 
- if eth_amount needed, eth_amount_in_wei = int(amount_in * (10**18))
- use buildTransaction method to generate a transaction 
'''


openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Generate a Python program to accomplish the following on-chain operations:"},
        {"role": "user", "content":  user_content},
    ],
    temperature = 0,
    pl_tags=["program_swap"]
)
