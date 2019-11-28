class TreeNode: 
	def __init__(self, val): 
	    self.val = val
	    self.left = None
	    self.right = None
	    self.height = 1
	    self.id = 0

class AVL_Tree: 

	def __init__(self):
		self.root = None
 
	def insert(self, root, key): 
	    if not root: 
	        self.root = TreeNode(key)
	        return self.root

	    elif key.getFee() < root.val.getFee(): 
	        root.left = self.insert(root.left, key) 
	    else: 
	        root.right = self.insert(root.right, key) 
	    root.height = 1 + max(self.getHeight(root.left), 
	                       self.getHeight(root.right)) 

	    balance = self.getBalance(root) 

	    if balance > 1 and key.getFee() < root.left.val.getFee(): 
	        return self.rightRotate(root) 

	    if balance < -1 and key.getFee() > root.right.val.getFee(): 
	        return self.leftRotate(root) 

	    if balance > 1 and key.getFee() > root.left.val.getFee(): 
	        root.left = self.leftRotate(root.left) 
	        return self.rightRotate(root) 

	    if balance < -1 and key.getFee() < root.right.val.getFee(): 
	        root.right = self.rightRotate(root.right) 
	        return self.leftRotate(root) 

	    return root

	def delete(self, root, key): 

	    if not root: 
	        return root 

	    elif key < root.val.getID(): 
	        root.left = self.delete(root.left, key) 

	    elif key > root.val.getID(): 
	        root.right = self.delete(root.right, key) 

	    else: 
	        if root.left is None: 
	            temp = root.right 
	            root = None
	            return temp 

	        elif root.right is None: 
	            temp = root.left 
	            root = None
	            return temp 

	        temp = self.getMinValueNode(root.right) 
	        root.val = temp.val
	        root.right = self.delete(root.right, 
	                                  temp.val) 

	    if root is None: 
	        return root 

	    root.height = 1 + max(self.getHeight(root.left), 
	                        self.getHeight(root.right)) 

	    balance = self.getBalance(root) 

	    if balance > 1 and self.getBalance(root.left) >= 0: 
	        return self.rightRotate(root) 

	    if balance < -1 and self.getBalance(root.right) <= 0: 
	        return self.leftRotate(root) 

	    if balance > 1 and self.getBalance(root.left) < 0: 
	        root.left = self.leftRotate(root.left) 
	        return self.rightRotate(root) 

	    if balance < -1 and self.getBalance(root.right) > 0: 
	        root.right = self.rightRotate(root.right) 
	        return self.leftRotate(root) 

	    return root 

	def leftRotate(self, z): 

	    y = z.right 
	    T2 = y.left 

	    y.left = z 
	    z.right = T2 

	    z.height = 1 + max(self.getHeight(z.left), 
	                     self.getHeight(z.right)) 
	    y.height = 1 + max(self.getHeight(y.left), 
	                     self.getHeight(y.right)) 

	    return y 

	def rightRotate(self, z): 

	    y = z.left 
	    T3 = y.right 

	    y.right = z 
	    z.left = T3 

	    z.height = 1 + max(self.getHeight(z.left), 
	                    self.getHeight(z.right)) 
	    y.height = 1 + max(self.getHeight(y.left), 
	                    self.getHeight(y.right)) 

	    return y 

	def getHeight(self, root): 
	    if not root: 
	        return 0

	    return root.height 

	def getBalance(self, root): 
	    if not root: 
	        return 0

	    return self.getHeight(root.left) - self.getHeight(root.right)

	def getMinValueNode(self, root): 
	    if root is None or root.left is None: 
		    return root 

	    return self.getMinValueNode(root.left)

	def search(self, root, data): 

	    if not root:
	    	return False

	    if data == root.val.getID():
	    	return True

	    if data < root.val.getID():
	    	return self.search(root.left, data)

	    else:
	    	return self.search(root.right, data)

	def inorder(self, root):

		if not root:
			return 

		self.inorder(root.left)

		print root.val.getID(), root.val.getSender(), root.val.getReceiver(), root.val.getFee(), root.val.getAmount()

		self.inorder(root.right)

	def getNode(self, root, data):

		if root.val.getID() == data:
			return root.val

		elif data < root.val.getID():
			return self.getNode(root.left, data)

		else:
			return self.getNode(root.right, data)