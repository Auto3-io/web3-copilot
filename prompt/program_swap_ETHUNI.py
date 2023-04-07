import promptlayer
import os
promptlayer.api_key = os.environ['PROMPT_API_KEY']

# Swap out your 'import openai'
openai = promptlayer.openai
openai.api_key = os.environ['OPENAI_API_KEY']

user_content = '''
1. Swap 0.01 ETH for UNI using Uniswap on Ethereum:
- Contract address: 0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D
- Method: swapETHForExactTokens
- ABI: '[{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"}]'
- Documentation: Swaps an exact amount of input tokens for as many output tokens as possible...

Related ERC20:
1. UNI (0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984)
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
    pl_tags=["program_swap_ETHUNI"]
)
