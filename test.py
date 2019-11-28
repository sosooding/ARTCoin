from os import chmod
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import transaction, block, blockchain, miner, AVLtree, network, user

key = RSA.generate(2048)
privatek = (key.exportKey('PEM'))
pubkey = key.publickey()
public = pubkey.exportKey('OpenSSH')

t = transaction.Transaction(0, 1, 25)
t2 = transaction.Transaction(1, 0, 30)
t.signTransaction(privatek, public)
t2.signTransaction(privatek, public)

'''
b = block.Block()
b.addTransaction(t)
b.addTransaction(t2)

b2 = block.Block()
b2.addTransaction(t2)
b2.addTransaction(t)

m = miner.Miner()
m.startMining(b)
m.startMining(b2)

bc = blockchain.Blockchain()
print bc.addBlock(b2)
'''

n = network.Network()
n.addTransaction(t)
n.addTransaction(t2)
n.showTransactions()

'''

t = AVLtree.AVL_Tree()
root = None
root = t.insert(root, 1)
root = t.insert(root, 2)
root = t.insert(root, 3)
print t.search(root, 2)
root = t.delete(root, 2)
print t.search(root, 2)
'''

user1 = user.User("rishik", "ajay")
user2 = user.User("rishik", "ajay")
n.addUser(user1)
n.addUser(user2)

m2 = miner.Miner(user2.getID())
m1 = miner.Miner(user1.getID())

m1.makeBlock(n)

print user1.getBalance()
print user2.getBalance()

n.showTransactions()

user1.processUpdates()
user1.showLedger()