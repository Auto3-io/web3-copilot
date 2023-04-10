from copilot.data.loader import get_erc20_address, get_contract_address


def test_erc20_get_address():
    token_name = 'USDT'
    chain_name = 'ethereum'
    address = get_erc20_address(token_name, chain_name)
    assert address == '0xdac17f958d2ee523a2206206994597c13d831ec7'

def test_contract_address():
    contract_name = 'SwapRouter'
    address = get_contract_address('UniswapV3', 'Ethereum', contract_name)
    assert address == '0xE592427A0AEce92De3Edee1F18E0157C05861564'

    address = get_contract_address('UniswapV2', 'Ethereum', "UniswapV2Router02")


test_contract_address()