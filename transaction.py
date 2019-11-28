"""
Class to implement transactions.

Requirements:
	:module: datetime
	:module: Crypto.Hash
	:module: Crypto.Signature
	:module: Crypto.PublicKey
"""

import datetime
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA

class Transaction:

	def __init__(self, receiver = None, sender = None, amount = 0, ownerPK = None, fee = 0):

		self.sender = sender
		self.receiver = receiver
		self.amount = amount
		self.hash = None
		self.signature = None
		self.fee = 0
		self.id = 0

	def signTransaction(self, private_key, public_key):

		message = str(self.sender) + ' ' + str(self.receiver) + ' ' + str(self.amount)
		digest = SHA256.new()
		digest.update(message)
		self.hash = digest.hexdigest()

		private_key = RSA.importKey(private_key)

		self.signature = PKCS1_v1_5.new(private_key).sign(digest)

		print "Signed Successfully!"

	def isSigned(self):
		return self.getSignature() != None

	def verifyTransaction(self, private_key):
		return PKCS1_v1_5.new(RSA.importKey(private_key).publickey()).verify(self.hash, self.signature)

	def getSender(self):
		return self.sender

	def getReceiver(self):
		return self.receiver

	def getAmount(self):
		return self.amount

	def getHash(self):
		return self.hash

	def getSignature(self):
		return self.signature

	def setFee(self, fee):
		self.fee = fee 

	def getFee(self):
		return self.fee

	def setID(self, ID):
		self.id = ID

	def getID(self):
		return self.id
