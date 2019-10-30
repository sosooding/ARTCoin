class Miner:

	def startMining(self, givenBlock, start = 1, end = 1000000):
		for nonce in range(start, end + 1):
			if givenBlock.checkSolution(nonce):
				return nonce