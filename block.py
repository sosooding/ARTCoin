"""
Class to implement a block

Requirements:
	:module: transaction
	:module: merkletree
	:module: Crypto.Hash
	:module: helperfunctions
"""


import transaction, merkletree, datetime, helperfunctions
from Crypto.Hash import SHA256

class Block:

	def __init__(self, index = 0, prev_hash = '0000000000000000000000000000000000000000000000000000000000000000', difficulty = 3, max_nodes = 256):

		'''
		Constructor function to generate a block.
		Default block is the genesis block.
		'''

		self.index = index
		self.prev_hash = prev_hash
		self.merkle_tree = merkletree.MerkleTree(max_nodes)
		self.nonce = 1
		self.difficulty = difficulty
		self.transactions = []
		self.next = None
		self.time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		self.hash = '0000000000000000000000000000000000000000000000000000000000000000'
		self.__addedToChain = False

		#self.forked_blocks = []

	def setIndex(self, idx):
		self.index = idx

	def getIndex(self):
		return self.index

	def setPrevHash(self, new_hash):
		self.prev_hash = new_hash

	def getPrevHash(self):
		return self.prev_hash

	def getMerkleRoot(self):
		return self.merkle_tree.merkleRoot()

	def __setNonce(self, nonce):
		self.nonce = nonce

	def getNonce(self):
		return self.nonce

	def setDifficulty(self, difficulty):
		self.difficulty = difficulty

	def addTransaction(self, cur_transaction):

		'''
		If the current block has space for adding another transaction,
		then adds the cur_transaction to the block.

		:param cur_transaction: Address of the transaction to be added
		:return: Return True if the transaction is added to the block 
				 otherwise False
		:rtype: bool
		'''
		
		if self.merkle_tree.insert(cur_transaction):
			self.transactions.append(cur_transaction)
			self.__createHash()
			return True

		else:
			return False

	def getTransactions(self):
		return self.transactions

	def setNextBlock(self, new_block):

		'''
		Attaches a new block to the current block after validating the 
		mining of the current block.

		:param new_block: Address of the new block that is trying to get
						  attached

		:return: Return True if the new block is attached successfully,
				 otherwise False.
		:rtype: bool
		'''

		if not self.checkSolution():
			print "Mine the current block first."
			return False

		if self.getStatus():
			print "Already in a chain"
			return False

		new_block.setPrevHash(self.getHash())
		self.next = new_block

		return True

	def getNextBlock(self):
		return self.next

	def getTimeStamp(self):
		return self.time_stamp

	'''
	def forkBlock(self, newBlock):
		self.forked_blocks.append(newBlock)

	def getForkedBlocks(self):
		return self.forked_blocks
	'''

	def setHash(self, givenHash):
		self.hash = givenHash

	def getHash(self):
		return self.hash

	def __resetHash(self):
		self.hash = None

	def __createHash(self):

		'''
		Generates a SHA256 hash of the current block and assign it to
		the hash of the block.
		
		The hash is created from:
			1. Hash of the previous block
			2. Merkle Root of the current block
			3. Time stamp of the current block
			4. Nonce
		'''

		hash_obj = SHA256.new()
		hash_obj.update(self.getPrevHash())
		hash_obj.update(self.getMerkleRoot())
		hash_obj.update(self.getTimeStamp())
		hash_obj.update(str(self.getNonce()))
		
		self.hash = hash_obj.hexdigest()

	def checkSolution(self, nonce = None):

		'''
		Checks if the given nonce is a valid solution to the block
		based on the difficulty possessed by the block.

		A nonce is a valid solution if the start of resulting hash of 
		the block has leading zeroes, greater than or equal to the 
		difficulty.

		If a nonce is passed, then the functions checks the validity of
		the given nonce, otherwise it simply uses the nonce that was used
		before.

		If a nonce is valid, then the hash is refreshed.

		:return: Return True if the nonce is a valid solution, otherwise
				 return False.
		:rtype:  bool
		'''

		if nonce == None:
			nonce = self.nonce

		if not nonce:
			self.__resetHash()
			return False

		self.__setNonce(nonce)
		self.__createHash()
		
		if helperfunctions.countZeroes(self.getHash()) >= self.difficulty:
			return True
			
		else:
			self.__resetHash()
			return False

	def setStatus(self, status):
		self.__addedToChain = status

	def getStatus(self):
		return self.__addedToChain