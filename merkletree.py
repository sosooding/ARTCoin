"""
Implementation of the MerkleTree using Segment Trees, without pruning.

Requirements:
	:module: math
	:module: Crypto.Hash
"""

from math import ceil, log
from Crypto.Hash import SHA256

class MerkleTree:

	def __init__(self, max_nodes):

		'''
		Constructor function initializes the MerkleTree and assigns
		the initial merkle root without any transactions as the SHA256 hash
		of '0000...000'.

		:param max_nodes: Maximum number of nodes at the last level.
						  Is modified to the least power of 2 greater than
						  of equal to max_nodes.
		'''

		self.node_cnt = 0
		self.max_nodes = pow(2, int(ceil(log(max_nodes, 2))))
		self.tree = [None for _ in range(2*self.max_nodes)]

		temp_digest = SHA256.new()
		temp_digest.update('0000000000000000000000000000000000000000000000000000000000000000')
		temp_digest = temp_digest.hexdigest()

		self.tree[1] = temp_digest

	def insert(self, data):

		'''
		If the maximum number of nodes have already been inserted, then
		return False.
		'''

		if self.node_cnt == self.max_nodes:
			return False

		else:
			self.__update(1, 0, self.max_nodes - 1, self.node_cnt, data)
			self.node_cnt += 1
			return True

	def __update(self, cur_root, left, right, pos, data):

		if left == right:
			self.tree[cur_root] = data.getHash()

		else:
			mid = (left + right)/2
			node_digest = SHA256.new()

			if pos <= mid:
				self.__update(cur_root*2, left, mid, pos, data)
			else:
				self.__update(cur_root*2 + 1, mid + 1, right, pos, data)

			if self.tree[cur_root*2] == None and self.tree[cur_root*2 + 1] == None:
				node_digest.update('0000000000000000000000000000000000000000000000000000000000000000')

			elif self.tree[cur_root*2] == None and self.tree[cur_root*2 + 1] != None:
				node_digest.update(self.tree[cur_root*2 + 1])
				node_digest.update(self.tree[cur_root*2 + 1])

			elif self.tree[cur_root*2] != None and self.tree[cur_root*2 + 1] == None:
				node_digest.update(self.tree[cur_root*2])
				node_digest.update(self.tree[cur_root*2])

			else:
				node_digest.update(self.tree[cur_root*2])
				node_digest.update(self.tree[cur_root*2 + 1])

			self.tree[cur_root] = node_digest.hexdigest()

	def merkleRoot(self):
		return self.tree[1]

	def getCountNodes(self):
		return self.node_cnt

	def getMaxNodes(self):
		return self.max_nodes
