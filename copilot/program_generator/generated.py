from web3 import Web3
import json

# Connect to the Ethereum network using Web3
web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/{your-infura-project-id}"))

# Set up the contract and function data for Uniswap v2 swapExactTokensForTokens
uniswap_contract_address = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"
uniswap_contract_abi = json.loads('{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"}')
uniswap_contract = web3.eth.contract(address=web3.toChecksumAddress(uniswap_contract_address), abi=uniswap_contract_abi)
uniswap_function = uniswap_contract.functions.swapExactTokensForTokens

# Set up the contract and function data for ERC20 USDC 
usdc_contract_address = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
usdc_contract_abi = json.loads('{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"minter","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"MinterAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"minter","type":"address"}],"name":"MinterRemoved","type":"event"},{"inputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"symbol","type":"string"},{"internalType":"uint8","name":"decimals","type":"uint8"},{"internalType":"address","name":"newOwner","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleBearers","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isMinter","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"addMinter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"renounceMinter","outputs":[],"stateMutability":"nonpayable","type":"function"}')
usdc_contract = web3.eth.contract(address=web3.toChecksumAddress(usdc_contract_address), abi=usdc_contract_abi)

# Set up the contract and function data for Aave deposit
aave_contract_address = "0x67890..."
aave_contract_abi = json.loads('{"anonymous":false,"inputs":[{"indexed":false,"name":"_reserve","type":"address"},{"indexed":false,"name":"_user","type":"address"},{"indexed":false,"name":"_amount","type":"uint256"}],"name":"Deposit","type":"event","signature":"0x5548c837ab068cf56a2c2479df0882a4922fd203edb7517321831d95078c5f62"}')
aave_contract = web3.eth.contract(address=web3.toChecksumAddress(aave_contract_address), abi=aave_contract_abi)
aave_function = aave_contract.functions.deposit

# Set up user addresses and private keys
user_address = "0xABCDEF..."
user_private_key = "0x123456..."

# Set up transfer address for sending half of the acquired ETH to
transfer_address = "0x123..."

# Define token amounts and deadlines
usdc_amount = 1000 * 10**6 # 1000 USDC in 6 decimal places
deadline = 1630878000 # Unix timestamp for deadline (in this case, 12:00 AM UTC on Sept 6, 2021)

# Approve the Uniswap contract to spend USDC on behalf of the user
usdc_approve_amount = uniswap_contract.functions.getAmountsOut(usdc_amount, 
    ['0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48', '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'])[1]
usdc_approve_function = usdc_contract.functions.approve(
    web3.toChecksumAddress(uniswap_contract_address), usdc_approve_amount)
usdc_approve_nonce = web3.eth.get_transaction_count(user_address)
usdc_approve_transaction = usdc_approve_function.buildTransaction({
    'chainId': web3.eth.chain_id,
    'gas': 200000,
    'gasPrice': web3.eth.gas_price,
    'nonce': usdc_approve_nonce
})
signed_usdc_approve_transaction = web3.eth.account.sign_transaction(
    usdc_approve_transaction, user_private_key)
web3.eth.send_raw_transaction(signed_usdc_approve_transaction.rawTransaction)

# Swap USDC for ETH using Uniswap
uniswap_input_tokens = [usdc_contract_address, web3.toChecksumAddress('0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2')] # USDC to ETH
uniswap_output_tokens = uniswap_function.call({'from': user_address}, 
    usdc_amount, 0, uniswap_input_tokens, user_address, deadline)
uniswap_function_nonce = web3.eth.get_transaction_count(user_address)
uniswap_transaction = uniswap_function.buildTransaction({
    'chainId': web3.eth.chain_id,
    'gas': 2000000,
    'gasPrice': web3.eth.gas_price,
    'nonce': uniswap_function_nonce,
    'args': [usdc_amount, 0, uniswap_input_tokens, user_address, deadline]
})
signed_uniswap_transaction = web3.eth.account.sign_transaction(
    uniswap_transaction, user_private_key)
web3.eth.send_raw_transaction(signed_uniswap_transaction.rawTransaction)

# Send half of acquired ETH to transfer address
eth_amount = uniswap_output_tokens[1] // 2
transfer_function = web3.eth.transfer(to=web3.toChecksumAddress(transfer_address), value=eth_amount)
transfer_nonce = web3.eth.get_transaction_count(user_address)
transfer_transaction = transfer_function.buildTransaction({
    'chainId': web3.eth.chain_id,
    'gas': 21000,
    'gasPrice': web3.eth.gas_price,
    'nonce': transfer_nonce
})
signed_transfer_transaction = web3.eth.account.sign_transaction(
    transfer_transaction, user_private_key)
web3.eth.send_raw_transaction(signed_transfer_transaction.rawTransaction)

# Approve Aave contract to spend acquired ETH on behalf of the user
aave_approve_amount = aave_contract.functions.getAmountsIn(eth_amount, '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2')[0]
aave_approve_function = web3.eth.contract(address=web3.toChecksumAddress('0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'), abi=usdc_contract_abi).functions.approve(
    web3.toChecksumAddress(aave_contract_address), aave_approve_amount)
aave_approve_nonce = web3.eth.get_transaction_count(user_address)
aave_approve_transaction = aave_approve_function.buildTransaction({
    'chainId': web3.eth.chain_id,
    'gas': 200000,
    'gasPrice': web3.eth.gas_price,
    'nonce': aave_approve_nonce
})
signed_aave_approve_transaction = web3.eth.account.sign_transaction(
    aave_approve_transaction, user_private_key)
web3.eth.send_raw_transaction(signed_aave_approve_transaction.rawTransaction)

# Deposit remaining ETH to Aave
aave_function_nonce = web3.eth.get_transaction_count(user_address)
aave_transaction = aave_function.buildTransaction({
    'chainId': web3.eth.chain_id,
    'gas': 2000000,
    'gasPrice': web3.eth.gas_price,
    'nonce': aave_function_nonce,
    'args': ['0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2', user_address, eth_amount, 0]
})
signed_aave_transaction = web3.eth.account.sign_transaction(
    aave_transaction, user_private_key)
web3.eth.send_raw_transaction(signed_aave_transaction.rawTransaction)
