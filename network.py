import random
import user
import Queue
import AVLtree

class Network:

	def __init__(self):

		self.users = []
		self.graph = []
		self.unverified_transactions_root = None
		self.unverified_transactions_tree = AVLtree.AVL_Tree()

	def getNumOfUsers(self):
		return len(self.users)

	def addUser(self, cur_user):

		cur_user.setID(self.getNumOfUsers())
		self.users.append(cur_user)
		self.graph.append([])
		self.connectToNeighbours(cur_user)

	def connectToNeighbours(self, cur_user):
		if self.getNumOfUsers() > 1:
			numOfNeighbours = random.randint(1, self.getNumOfUsers() - 1)
			for i in range(numOfNeighbours):
				while True:
					person_1, person_2 = cur_user.getID(), random.randint(0, self.getNumOfUsers() - 1)
					if person_1 != person_2 and person_2 not in self.graph[person_1]:
						self.addNeighbour(person_1, person_2)
						break
			return True

		return False

	def addNeighbour(self, person_1, person_2):

		self.graph[person_1].append(person_2)
		self.graph[person_2].append(person_1)

	def addTransaction(self, transac):

		ID = 1
		while self.unverified_transactions_tree.search(self.unverified_transactions_root, ID) != False:
			ID += 1

		transac.setID(ID)
		self.unverified_transactions_root = self.unverified_transactions_tree.insert(self.unverified_transactions_root, transac)

	def removeTransaction(self, transacID):

		self.unverified_transactions_tree.delete(self.unverified_transactions_root, transacID)

	def searchTransaction(self, transacID):

		return self.unverified_transactions_tree.search(self.unverified_transactions_root, transacID)

	def getTransaction(self, transacID):

		return self.unverified_transactions_tree.getNode(self.unverified_transactions_root, transacID)

	def removeVerifiedTransactions(self, blk):

		self.showTransactions()

		sum_of_fee = 0

		for i in blk.getTransactions():
			self.unverified_transactions_root = self.unverified_transactions_tree.delete(self.unverified_transactions_root, i.getID())
			self.users[i.getSender()].subtractBalance(i.getAmount())
			self.users[i.getReceiver()].addBalance(i.getAmount())
			sum_of_fee += i.getFee()

		return sum_of_fee

	def broadcastBlock(self, blk, user):
		
		vis = [False for i in range(self.getNumOfUsers())]

		q = Queue.Queue()
		q.put(user)
		vis[user] = True
		self.users[user].addUpdate(blk)

		while not q.empty():
			node = q.get()

			for i in self.graph[node]:
				if not vis[i]:
					vis[i] = True
					q.put(i)
					self.users[i].addUpdate(blk)

		self.users[user].addBalance(self.removeVerifiedTransactions(blk))
		self.users[user].addBalance(8)

	def showTransactions(self):

		self.unverified_transactions_tree.inorder(self.unverified_transactions_root)
