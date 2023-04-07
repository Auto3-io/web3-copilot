from copilot.data.loader import get_erc20_address


def test_erc20_get_address():
    token_name = 'USDT'
    chain_name = 'ethereum'
    address = get_erc20_address(token_name, chain_name)
    assert address == '0xdac17f958d2ee523a2206206994597c13d831ec7'
