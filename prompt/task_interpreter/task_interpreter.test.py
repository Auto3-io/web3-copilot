from prompt.task_interpreter import task_interpreter

user_requirement = 'Swap 1000 USDC for ETH in Ethereum, then send half to 0x123, and deposit the rest to Aave'

resp = task_interpreter(user_requirement)

print(resp)