# import necessary libraries and constants
import json
from web3 import Web3
from eth_account import Account

MY_ADDRESS = "ENTER YOUR WALLET ADDRESS HERE" # address of your Ethereum wallet
PRIVATE_KEY = "ENTER YOUR PRIVATE KEY HERE" # private key for your Ethereum wallet
UNISWAP_V2_ROUTER_ADDRESS = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D" # address of Uniswap V2 Router
UNISWAP_V2_ROUTER_ABI = json.load(open("UNISWAP_ROUTERV2.json")) # ABI for Uniswap V2 Router
ERC20_ABI = json.load(open("ERC20.json")) # ABI for ERC20 contracts
USDC_ADDRESS = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48" # address of USDC contract
WETH_ADDRESS = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2" # address of WETH contract
GAS_PRICE = Web3.toWei("100", "gwei") # gas price in Wei
GAS_LIMIT = 3000000 # maximum gas limit for the transaction

# connect to the Ethereum network via Infura node
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/ENTER_YOUR_INFURA_PROJECT_ID"))

def swap_USDC_for_ETH(amount):
    """A function to swap USDC for ETH on Uniswap V2"""
    # create contract instances
    uniswap_router = w3.eth.contract(
        address=UNISWAP_V2_ROUTER_ADDRESS, abi=UNISWAP_V2_ROUTER_ABI
    )
    usdc = w3.eth.contract(address=USDC_ADDRESS, abi=ERC20_ABI)

    # get the amount of USDC to swap in Wei
    decimals = usdc.functions.decimals().call()
    amountInWei = Web3.toWei(amount, "ether") * 10 ** decimals

    # check the allowance of the Uniswap Router for USDC
    allowance = usdc.functions.allowance(MY_ADDRESS, UNISWAP_V2_ROUTER_ADDRESS).call()

    # approve the Uniswap Router to spend USDC if allowance is insufficient
    if allowance < amountInWei:
        approve_txn = usdc.functions.approve(
            UNISWAP_V2_ROUTER_ADDRESS, amountInWei
        ).buildTransaction(
            {
                "from": MY_ADDRESS,
                "gas": GAS_LIMIT,
                "gasPrice": GAS_PRICE,
                "nonce": w3.eth.getTransactionCount(MY_ADDRESS),
            }
        )
        signed_approve_txn = Account.sign_transaction(approve_txn, PRIVATE_KEY)
        approve_txn_hash = w3.eth.sendRawTransaction(signed_approve_txn.rawTransaction)
        w3.eth.waitForTransactionReceipt(approve_txn_hash)
        print(f"Approved Uniswap Router to spend {amount} USDC")

    # swap USDC for ETH on Uniswap V2
    swap_txn = uniswap_router.functions.swapExactTokensForETH(
        amountInWei,
        0,
        [USDC_ADDRESS, WETH_ADDRESS],
        MY_ADDRESS,
        w3.eth.getBlock('latest').timestamp + 100,
    ).buildTransaction(
        {
            "from": MY_ADDRESS,
            "gas": GAS_LIMIT,
            "gasPrice": GAS_PRICE,
            "nonce": w3.eth.getTransactionCount(MY_ADDRESS),
        }
    )
    signed_swap_txn = Account.sign_transaction(swap_txn, PRIVATE_KEY)
    swap_txn_hash = w3.eth.sendRawTransaction(signed_swap_txn.rawTransaction)
    print(f"Swapping {amount} USDC for ETH...")
    w3.eth.waitForTransactionReceipt(swap_txn_hash)

# call the function to swap USDC for ETH
swap_USDC_for_ETH(1000) # amount in USDC to swap to ETH