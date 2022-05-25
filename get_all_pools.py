from web3 import HTTPProvider, Web3
from web3.contract import Contract
from web3._utils.filters import LogFilter
from env import INFURAHTTPS

w3 = Web3(HTTPProvider(INFURAHTTPS))
a = open("UniswapV3abi.json", 'r')
address = '0x1F98431c8aD98523631AE4a59f267346ea31F984'
abi = a.read()
contract_instance: Contract = w3.eth.contract(address=address, abi=abi)
Pool_filter: LogFilter = contract_instance.events.PoolCreated.createFilter(fromBlock="0x0")
all_pool_creation_events = Pool_filter.get_all_entries()
with open("pools.txt", "w") as file: 
    for i in all_pool_creation_events:
        file.write(i['args']["token0"] + " ")
        file.write(i['args']["token1"] + " ")
        file.write(i['args']['pool'] + " ")
        file.write("\n")
