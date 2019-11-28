import block

class Miner:

	def __init__(self, ID):

		self.allBlocks = []
		self.id = ID

	def mine(self, givenBlock, start = 1, end = 100000000):
		for nonce in xrange(start, end + 1):
			if givenBlock.checkSolution(nonce):
				print "Success at :", nonce
				return nonce
			else:
				print "Failed at :", nonce
				
	def getID(self):
		return self.id

	def makeBlock(self, network):

		s = set()

		network.showTransactions()

		print "Enter number of transactions you want in the block: "
		numOfTransactions = input()

		while len(s) < numOfTransactions:
			ID = input("Enter an ID: ")
			if network.searchTransaction(ID):
				s.add(ID)

		self.allBlocks.append(block.Block())

		for i in list(s):
			self.allBlocks[-1].addTransaction(network.getTransaction(i))

		network.broadcastBlock(self.allBlocks[-1], self.getID())
