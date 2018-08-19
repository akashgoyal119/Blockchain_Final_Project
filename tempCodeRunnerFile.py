for contract in contract_pool.list:
       user_1.accept_bet(contract.contract_hash_value, contract_pool, txn_memory_pool)

    print(txn_memory_pool.list)

    miner_1 = Miner()
    
    genesis_block = Block.generate_genesis_block()
    print(genesis_block)
