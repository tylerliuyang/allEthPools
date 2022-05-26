from typing import List
from web3 import HTTPProvider, Web3
from web3.contract import Contract
from web3._utils.filters import LogFilter
from env import INFURAHTTPS

w3 = Web3(HTTPProvider(INFURAHTTPS))
a = open("shibaswap_abi.json", 'r')
address = '0x03f7724180AA6b939894B5Ca4314783B0b36b329'
abi = a.read()
contract_instance: Contract = w3.eth.contract(address=address, abi=abi)

def get_reserve_amount(address: str) -> List: 
    a = open("shibapool_abi.json", 'r')
    abi = a.read()
    contract_instance: Contract = w3.eth.contract(address=address, abi=abi)
    return contract_instance.functions.getReserves().call()
address = input("enter SSLP contract address:")
reserve_amount = get_reserve_amount(address)
print(reserve_amount)
print(contract_instance.functions.getAmountOut(1, reserve_amount[0], reserve_amount[1]).call(), "token0 to token1")
print(contract_instance.functions.getAmountOut(1, reserve_amount[1], reserve_amount[0]).call(), "token1 to token0")
