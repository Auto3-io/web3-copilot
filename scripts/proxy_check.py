import csv
import time
from web3 import Web3

# 连接到以太坊节点
web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/d65cbc952b854854b6a2a08708057072'))

# 检查是否为代理合约的代码前缀
proxy_code_prefix = '73b4'
i=1
# 读取合约地址列表
with open('D:/constrac_accresses.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        contract_address = row['contract_address']
        print(f'Checking {contract_address}...')

        # 将地址转换为checksum地址
        checksum_address = web3.to_checksum_address(contract_address)

        # 获取合约的代码
        code = web3.eth.get_code(checksum_address)


        # 检查代码是否为代理合约
        if proxy_code_prefix in code.hex():
            print(f'{i}   1.')
        else:
            print(f'{i}   0.')
        i=i+1
        time.sleep(1)