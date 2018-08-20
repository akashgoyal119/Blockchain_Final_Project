MPCS 56600 - Introduction to Blockchain

TEAM PROJECT

TEAM MEMBERS: Akash Goyal, Yilun Hu, Zhihuang Chen, Jae-Yeun Hwang
======================================

NOTE: Please execute the program using Python3.6

======================================

1. INTRODUCTION
---------------
a) MagicCoins
    - The name of the CryptoCurrency is 'MagicCoins'.
    - The smallest unit is called: 'quidditch'.
    - 1 MagicCoin = 1000 quidditch


b) NAME OF OUR GAMBLING SYSTEM


b) Docker Images
    - DNS_SEED and FULL_NODE images are zipped and uploaded to the
    directory "/stage/MPCS56600/jaeyeun"; download and unzip both files.


c) Source Codes (Python 3.6)

    - The python codes are inside the "src" directory.
        1) DNS_SEED.py : DNS_SEED server codes.
        2) FullNode.py : FULL_NODE client/server codes.
        3) regstrar.proto : DNS_SEED server protocol.
        4) full_node.proto : FULL NODE client/server protocol.
        5) other files: automatically generated files from gRPC.

    - The python codes for MagicCoin crypto-currency are inside the "src/MagicCoin/" directory.
        1) python codes for BlockChain class: "MC_BlockChain.py"
        2) python codes for Block class: "MC_Block.py"
        3) python codes for Header class: "MC_Header.py"
        4) python codes for Transaction class: "MC_Transaction.py"
        5) python codes for TxnMemoryPool class: "MC_TxnMemoryPool.py"
        6) python codes for Output class: "MC_Output.py"
        7) python codes for Minder class: "MC_Miner.py"
        8) python codes for User class: "MC_User.py"
        9) python codes for Contract class: "MC_Contract.py"
        10) python codes for ContractMemoryPool class: "MC_ContractMemoryPool.py"


2. STARTING THE DNS_SEED SERVER
-------------------
a) Start 1 docker container with DNS_SEED image and name it DNS_SEED.

b) In terminal (for example):

    - execute: "docker run -it --hostname dns_seed --name DNS_SEED 1d5762ed56db /bin/bash"

c) In the container, cd into "Blockchain_Final_Project" directory:

    - execute: "cd Blockchain_Final_Project"

d) In the container's "Blockchain_Final_Project" directory:

    - execute: "python3.6 DNS_SEED.py"

e) You should see a message that says: 

    - "... Start DNS SEED server ..."


3. STARTING THE FULL_NODE CLIENT/SERVER
-------------------
a) Start 3 docker containers with FULL_NODE image and name each of them
   FULL_NODE_1, FULL_NODE_2, FULL_NODE_3.

b) For each container, in terminal (for example, for FULL_NODE_1):

    - execute: "docker run -it --hostname full_node_1 --name FULL_NODE_1 --link DNS_SEED:dns_seed 1d5762ed56db /bin/bash"

    - IMPORTANT NOTE: Need to link each of the FULL_NODE containers with the DNS_SEED container.

c) In the container, cd into "Blockchain_Final_Project" directory:

    - execute: "cd Blockchain_Final_Project"

d) In the container's "Blockchain_Final_Project" directory:

    - execute: "python3.6 FullNode.py"

e) You should see a message that looks something like: 

    - "Full Node IP Address: 172.17.0.5"


4. COMMENTS ABOUT THE SOURCE CODES (WHAT WORKED AND WHAT DIDN'T WORK)
-------------------
a) When a node joins the network, if it is the first node to join, then it 
   receives a null response from the DNS_SEED server, otherwise it receives the 
   ip address of the latest registered node from the DNS_SEED server.

b) Each of the node that joins the network initiates handshake with every other 
   node in the network exactly once.

c) When a node joins the network, it receives the missing blocks of the 
   blockchain from the latest-registered node. This ensures that the blockchain
   become eventually consistent for all of the nodes in the network. In order to 
   ensure the consistency of the blockchains in each of the mining node, I added 
   an extra protocol that calls the method "existing_block_broadcast()".

d) Each contract (or bet) is generated when two users agree upon a bet, and
   every contract that is generated is propagated throughout the network.

e) Each contract generates two transactions, one transaction going to the
   poster and the other transaction going from the poster. Both of these 
   transactions are propagated throughout the network and saved in each node's
   transaction memory pool.

f) After a contract's result has been verified (after a contract's check_result_time),
   only one of the two transactions will be deemed as valid and that contract will be
   added to the "valid transaction memory pool". Only the transactions in the
   "valid transaction memory pool" will be added to the blocks that are being mined.

g) When a node receives a transaction from another node, if the transaction 
   already exists in the node's transaction memory pool, the node discards 
   the transaction. But if the transaction new to the receiving node, then 
   the node adds the transaction to its memory pool and also broadcasts 
   the said transaction to other nodes, excluding the node that broadcasted
   the transaction, so that the transaction can propagate throughout the network.

h) When a node mines a new block, it broadcasts it to every other node in the network.

i) When a node receives a new block, it matches the block_hash value and adds
   the block to the blockchain.

j) When a node receives a new block and adds it to its blockchain while mining
   its own separate block, the node will immediately start mining a new block again.

k) When a node receives a new block and adds it to its blockchain, all the valid transactions 
   that was included in the new block will be removed from the node's local "valid transaction memory pool".
