import Queue
import blockchain
import AVLtree
import transaction
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import miner

class User:

	def __init__(self, name, password):

		self.name = name
		self.password = password
		self.private_key = None
		self.public_key = None
		self.balance = 0
		self.pending_updates = Queue.Queue()
		self.ledger = blockchain.Blockchain()
		self.id = None
		self.root = None

		self.createKeys()

	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name 

	def setPassword(self, password):
		self.password = password

	def checkPassword(self, guess):
		return self.password == guess

	def createKeys(self):

		key = RSA.generate(2048)
		self.private_key = (key.exportKey('PEM'))

		pubkey = key.publickey()
		self.public_key = pubkey.exportKey('OpenSSH')

		'''
		print "Private Key: "
		print self.getPrivateKey()

		print "Public Key: "
		print self.getPublicKey()
		'''
		
	def getPrivateKey(self):
		return self.private_key

	def getPublicKey(self):
		return self.public_key

	def addBalance(self, balance):
		self.balance += balance

	def subtractBalance(self, balance):
		self.balance -= balance

	def getBalance(self):
		return self.balance

	def addUpdate(self, update):
		self.pending_updates.put(update)

	def processUpdates(self):

		while not self.pending_updates.empty():
			self.ledger.addBlock(self.pending_updates.get())

	def getID(self):
		return self.id 

	def setID(self, ID):
		self.id = ID

	def doTransaction(self, receiver, amount, fee = 0):

		if receiver == None:
			return False

		if amount > self.balance:
			return False

		newTransac = transaction.Transaction(receiver, self.getPublicKey(), amount, self.getPublicKey(), fee)

	def showLedger(self):

		self.ledger.showChain()