"""
Class to implement the blockchain

Requirements:
	:module: block
	:module: miner
"""

import block
import miner

class Blockchain:

	def __init__(self):

		'''
		Constructor function that creates a genesis block as soon as the 
		Blockchain class is created.
		'''
		
		self.main_chain_genesis = None
		self.latest_block = None

		self.__createGenesisBlock()

		miner.Miner().startMining(self.main_chain_genesis)

	def __createGenesisBlock(self):

		'''
		Creates a genesis block and assigns it to the head and the tail
		of the blockchain.
		'''

		self.main_chain_genesis = block.Block()
		self.latest_block = self.main_chain_genesis

		print "Genesis block has been generated!"

	def validateNewBlock(self, new_block):

		'''
		Validates if the given block has been mined or not.

		:return: If the block has been mined, then return True otherwise
				 false.
		:rtype: bool
		'''

		return new_block.checkSolution()

	def updateChain(self):

		'''
		Updates the indices of the newly added blocks in the blockchain.
		'''

		i = self.latest_block.getIndex() + 1
		cur_block = self.latest_block.next

		while cur_block != None:
			cur_block.setIndex(i)
			cur_block = cur_block.next
			i += 1

	def validateChain(self):

		'''
		Validates if the current blockchain is a valid one or not.
		This helps to check if any block in the middle has not been tampered.

		:return: If the whole blockchain is valid, then return True otherwise
				 false.
		:rtype:  bool
		'''

		parent = self.main_chain_genesis
		cur_block = parent.next

		while cur_block != None:
			if cur_block.getPrevHash() != parent.getHash():
				return False
			parent, cur_block = cur_block, cur_block.next

		return True

	def addBlock(self, new_block):

		'''
		Adds a given new block to the blockchain after validation.
		Validations performed before adding the new block to the blockchain:
			validateNewBlock()
			validateChain()

		If the validations pass, then the new block is added to the blockchain
		and the latest_block is set to the last block in the current blockchain

		:param new_block: Address of the block trying to get attached.
		:return: If the new block has been successfully added, return True
				 otherwise false.
		:rtype: bool
		'''

		if self.validateNewBlock(new_block):

			'''
			To be implemented when expanding the project to handle multiple 
			requests in a short period of time.

			new_block.resolveConflicts()
			self.latest_block.forkBlock(new_block)
			'''

			self.latest_block.setNextBlock(new_block)
			self.updateChain()

			if self.validateChain():
				self.setLatestBlock(new_block)
				return True
			else:
				self.setLatestBlock(None)
				return False
		else:
			return False

	def getDepth(self):
		return self.latest_block.index

	def getLatestBlock(self):
		return self.latest_block

	def setLatestBlock(self, new_block):
		self.latest_block = new_block
