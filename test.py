from MagicCoin.MC_Block import Block
from MagicCoin.MC_BlockChain import BlockChain
from MagicCoin.MC_Contract import  Contract
from MagicCoin.MC_Output import Output
from MagicCoin.MC_ContractMemoryPool import ContractMemoryPool
from MagicCoin.MC_Output import Output
from MagicCoin.MC_Transaction import Transaction
from MagicCoin.MC_TxnMemoryPool import TxnMemoryPool
from MagicCoin.MC_User import User
from MagicCoin.MC_Miner import Miner
from MagicCoin.MC_Header import Header


def main():
    user_1 = User(public_key='23456tewrsg3ty5')
    contract_pool = ContractMemoryPool(10)
    #print(contract_pool.list)

    txn_memory_pool = TxnMemoryPool()
    for contract in contract_pool.list:
       user_1.accept_bet(contract.contract_hash_value, contract_pool, txn_memory_pool)

    #print(txn_memory_pool.list)
    miner_1 = Miner()
    
    genesis_block = Block.generate_genesis_block()
    print(genesis_block)
    print(txn_memory_pool.list)


if __name__ == '__main__':
    main()
