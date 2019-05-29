# Problem 5. Blockchain

For this problem I used a linked list of blocks named blockchain but in 
which the head points to the last element appened to the blockchain.
In order to get to the first block we need to follow the chain of blocks.

I took the following assumptions:
- when the blockchain is created, the first block called genesis is created
automatically since it is the only block that doesn't have a next block.

- when a block is added to the blockchain, we only allow to add data to 
the block. Other attributes such as timestamp or prev block hash are
managed internally by the blockchain class.

- block hash is generated with current's block timestamp, data and prev hash.

The complexity for the worst case to add a block is O(1) and to traverse 
the blockchain from head to genesis is O(n).

The space complexity is O(n) being n the number of blocks.